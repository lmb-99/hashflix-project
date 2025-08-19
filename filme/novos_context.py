#gerenciador de contexto
#smp colocar na parte de context do setting dps de criar uma nova classe
from .models import Filme


def lista_filmes_recentes(request):
    lista_filmes = Filme.objects.all().order_by('-data_criacao')[0:8]
    return {'lista_filmes_recentes': lista_filmes}

def lista_filmes_populares(request):
    lista_filmes = Filme.objects.all().order_by('-visualizacoes')[0:8]
    return {'lista_filmes_populares': lista_filmes}

def filme_destaque(request):
    lista_filmes = Filme.objects.all().order_by('-data_criacao')[0:8]
    if lista_filmes:
        filme_destaque = lista_filmes[0]
    else:
        filme_destaque = None
    return {'filme_destaque': filme_destaque}