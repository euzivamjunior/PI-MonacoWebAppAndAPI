from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('formulario', views.formulario, name='formulario'),
    path('servico/alinhamento', views.servico_alinhamento, name='servico_alinhamento'),
    path('servico/balanceamento', views.servico_balanceamento, name='servico_balanceamento'),
    path('servico/cambagem', views.servico_cambagem, name='servico_cambagem'),
    path('servico/escapamento', views.servico_escapamento, name='servico_escapamento'),
    path('servico/motor', views.servico_motor, name='servico_motor'),
    path('servico/pneu', views.servico_pneu, name='servico_pneu'),
    path('servico/suspencao', views.servico_suspencao, name='servico_suspencao'),
    path('servico/trocaoleo', views.servico_troca_oleo, name='servico_troca_oleo'),
    path('modelos', views.lista_modelos, name='lista_modelos'),
]
