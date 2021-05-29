from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Produto
# Class based views cria um formulário automáticamente com os campos da classe, ex: models = Produto


class IndexView(ListView):
    models = Produto
    template_name = 'index.html'
    queryset = Produto.objects.all()
    context_object_name = 'produtos'  # Qual o nome que vamos utilizar para recupera os dados no template


class CreateProdutoView(CreateView):
    model = Produto
    template_name = 'produto_form.html'
    fields = ['nome', 'preco']
    success_url = reverse_lazy('index')


class UpdateProdutoView(UpdateView):
    model = Produto
    template_name = 'produto_form.html'
    fields = ['nome', 'preco']
    success_url = reverse_lazy('index')


class DeleteProdutoView(DeleteView):
    model = Produto
    template_name = 'produto_del.html'
    success_url = reverse_lazy('index')
