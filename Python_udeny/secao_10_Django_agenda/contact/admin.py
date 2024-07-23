from django.contrib import admin
from contact import models
#  classe abaixo para formatar o form no admin do django.


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):  # herda de admin
    list_display = 'id', 'first_name', 'last_name', 'phone',
    ordering = '-id',  # ordem de 'id', o sinal '-' indica decrescente
    list_filter = 'created_date',  # filtro aparece ao lado dos dados no admin
    search_fields = 'id', 'first_name', 'last_name',
    list_per_page = 10  # quantidade por pagina
    list_max_show_all = 200  # qtd máxima para o 'listar tudo'
    list_editable = 'first_name', 'last_name'  # campos editáveis pelo form
    list_display_links = 'id', 'phone',
