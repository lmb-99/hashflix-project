from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

# toda mudanca feita no db tem q rodar um python manage.py makemigrations
# e dps um python manage.py migrate no terminal

# criar usuario

#1st item da tupla = oq vc armazena no db
#2nd item da tupla = oq vc mostra pro usuario
LISTA_CATEGORIAS = (
    ('ANALISES', 'Análises'),
    ('PROGRAMACAO', 'Programacao'),
    ('APRESENTACAO', 'Apresentacao'),
    ('OUTROS', 'Outros')
)

# criar filmes
class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(max_length=1000)
    thumb = models.ImageField(upload_to='thumb_filmes')
    categoria = models.CharField(max_length=15, choices=LISTA_CATEGORIAS)
    visualizacoes = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo


# criar episodios
class Episodio(models.Model):
    filme = models.ForeignKey('Filme', related_name='episodios', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    video = models.URLField()

    def __str__(self):
        return self.titulo

#o AbstractUser ja vem com email, senha, etc
class Usuario(AbstractUser):
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = []
  email = models.EmailField(unique=True)
  filmes_vistos = models.ManyToManyField('Filme')





