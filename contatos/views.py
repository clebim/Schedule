from django.shortcuts import render
from .models import Contato
from django.core.paginator import Paginator

# Create your views here.

def index(request):
  contatos = Contato.objects.all()
  paginator = Paginator(contatos, 10)
  page = request.GET.get('page')
  contatos = paginator.get_page(page)
  return render(request, 'pages/index.html',{
    'contatos': contatos
  })


def store(request, id):
  contato = Contato.objects.get(id=id)
  return render(request, 'pages/store.html',{
    'contato': contato
  })