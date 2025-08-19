from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django import forms

#criar o form padrao mas baseado no modelo do Usuario (criado por mim)

class CriarContaForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = Usuario
        fields = ('username', 'email', 'password1', 'password2')


class FormHomepage(forms.Form):
    email = forms.EmailField(label=False)