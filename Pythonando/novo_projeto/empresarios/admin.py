from django.contrib import admin
from .models import Empresas, Documento, Metricas
# Register your models here.

admin.site.register(Empresas)  # registra a tabela na area de admin.
admin.site.register(Documento)  # registra a tabela na area de admin.
admin.site.register(Metricas)  # registra a tabela na area de admin.
