from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, TemplateView
from django.shortcuts import render
from .models import Estoque
from core.forms import InsereItemForm


class HomeTemplateView(TemplateView):

    template_name = 'index.html'


class EstoqueListView(ListView):
    model = Estoque
    template_name = 'lista.html'
    context_object_name = "items"


class EstoqueCreateView(CreateView):
    template_name = "cria.html"
    model = Estoque
    form_class = InsereItemForm
    success_url = reverse_lazy("core:lista_items")


class EstoqueUpdateView(UpdateView):
    template_name = "atualiza.html"
    model = Estoque
    fields = '__all__'
    context_object_name = 'item'
    success_url = reverse_lazy("core:lista_items")


class EstoqueDeleteView(DeleteView):
    template_name = "exclui.html"
    model = Estoque
    fields = '__all__'
    context_object_name = 'item'
    success_url = reverse_lazy("core:lista_items")
