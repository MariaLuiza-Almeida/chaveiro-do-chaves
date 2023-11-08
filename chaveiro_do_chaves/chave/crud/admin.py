from django.contrib import admin

# Register your models here.
from .models import Chave, Servidor, Emprestimo
admin.site.register(Chave)
admin.site.register(Servidor)
admin.site.register(Emprestimo)