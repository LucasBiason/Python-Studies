from django.urls import path
from core.views import HomeTemplateView, EstoqueListView, \
    EstoqueUpdateView, EstoqueCreateView, \
    EstoqueDeleteView

app_name = 'core'

urlpatterns = [
    path('', HomeTemplateView.as_view(), name="home"),
    path('estoque/cadastrar', EstoqueCreateView.as_view(), name="cadastra_item"),
    path('estoque/', EstoqueListView.as_view(), name="lista_items"),
    path('estoque/<pk>', EstoqueUpdateView.as_view(), name="atualiza_item"),
    path('estoque/excluir/<pk>', EstoqueDeleteView.as_view(), name="deleta_item"),
]
