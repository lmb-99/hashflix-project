from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Filme, Episodio, Usuario

# Register your models here.

#só criamos a estrutura abaixo pq quero q o campo de filmes_vistos apareca no admin
campos = list(UserAdmin.fieldsets)
campos.append(
    ('Watch History', {'fields': ('filmes_vistos',)}),
)
UserAdmin.fieldsets = tuple(campos)

admin.site.register(Filme)
admin.site.register(Episodio)
admin.site.register(Usuario, UserAdmin)

