from django.contrib import admin
"""
from .models import Formulario
from oficina.filters import MyDateTimeFilter


class ListandoFormularios(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'telefone', 'marca_veiculo', 'modelo_veiculo',
                    'data_do_agendamento', 'confirmado', 'servico_realizado')
    list_display_links = ('nome', 'sobrenome', 'data_do_agendamento')
    search_fields = ('nome', 'telefone', 'data_do_agendamento')
    list_filter = (('data_do_agendamento', MyDateTimeFilter),)
    list_editable = ('confirmado', 'servico_realizado')
    list_per_page = 20


admin.site.register(Formulario, ListandoFormularios)
"""
