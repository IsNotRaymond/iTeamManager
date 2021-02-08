from django.contrib import admin
from .models import Categoria, Projeto, UsuarioAceito, UsuarioRecusado, UsuarioBanido, UsuarioGratificado, UsuarioAdvertido, UsuarioConvidado

admin.site.register(Categoria)
admin.site.register(Projeto)
admin.site.register(UsuarioAceito)
admin.site.register(UsuarioRecusado)
admin.site.register(UsuarioBanido)
admin.site.register(UsuarioGratificado)
admin.site.register(UsuarioAdvertido)
admin.site.register(UsuarioConvidado)
