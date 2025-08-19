from urllib import request
from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView, ListView, FormView, DetailView, UpdateView
from .forms import CriarContaForm, FormHomepage
from .models import Filme, Usuario
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

#def homepage(request):
#    return render(request, 'homepage.html')

#importando o templateview e listview pra fazer a classe dps eu tenho q obrigatoriamente ter a variavel template_name pra mostrar o template da pag
class Homepage(FormView):
    template_name = 'homepage.html'
    form_class = FormHomepage

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('filme:homefilmes') #pegar url= app:url (essa url é o name q vc deu no url.py)
        else:
            return super().get(request, *args, **kwargs) #vai redirecionar pra pag na classe

    def get_success_url(self):
        email = self.request.POST.get('email')
        usuarios = Usuario.objects.filter(email=email)
        if usuarios:
            return reverse('filme:login')
        else:
            return reverse('filme:criarconta')

#def homefilmes(request):
#    context = {}
#    lista_filmes = Filme.objects.all()
#    context['lista_filmes'] = lista_filmes
#    return render(request, 'homefilmes.html', context)

class Homefilmes(LoginRequiredMixin, ListView):
    template_name = 'homefilmes.html'
    model = Filme
    # nome vai ser object_list ->  lista de itens do models

class DetalhesFilmes(LoginRequiredMixin, DetailView):
    template_name = 'detalhesfilmes.html'
    model = Filme
    #object -> 1 item do nosso model

    def get(self, request, *args, **kwargs):
        #contabilizar uma visualizacao
        filme = self.get_object()
        filme.visualizacoes += 1
        filme.save() #pra salvar a alteracao no banco de dados
        usuario = request.user #smp q pega uma info do usuario, tem q fazer com o request -> request.user
        usuario.filmes_vistos.add(filme)
        return super().get(request, *args, **kwargs) #redireciona o usuario pra URL final

    def get_context_data(self, **kwargs):
        context = super(DetalhesFilmes, self).get_context_data(**kwargs)
        filmes_relacionados = Filme.objects.filter(categoria=self.get_object().categoria)[0:4]
        context['filmes_relacionados'] = filmes_relacionados
        return context

class PesquisaFilme(LoginRequiredMixin, ListView):
    template_name = 'pesquisa.html'
    model = Filme

    def get_queryset(self):
        termo_pesquisa = self.request.GET.get('query')
        if termo_pesquisa:
            object_list = self.model.objects.filter(titulo__icontains=termo_pesquisa)
            return object_list
        else:
            return None

class EditarPerfil(LoginRequiredMixin, UpdateView):
    template_name = 'editarperfil.html'
    model = Usuario
    fields = ['first_name', 'last_name', 'email']

    def get_success_url(self):
        return reverse('filme:homefilmes')

class CriarConta(FormView):
    template_name = 'criarconta.html'
    form_class = CriarContaForm

    def form_valid(self, form):
        form.save() #se vc nao salvar o form ele nao vai criar o usuario no db
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('filme:login')

# a funcao get_success_url espera um texto de link como return entao smp tem q usar o 'reverse', na maioria dos outros casos da pra
#usar um 'redirect' q so precisa q vc mostre pra onde a funcao tem q direcionar