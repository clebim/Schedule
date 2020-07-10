from django.shortcuts import render
from .models import Contato
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat

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

def busca(request):
  termo = request.GET.get('termo')
  campos = Concat('nome', Value(' '), 'sobrenome')

  contatos = Contato.objects.annotate(
    nome_completo = campos
  ).filter(
    nome_completo__icontains = termo
  )
  
  paginator = Paginator(contatos, 10)
  page = request.GET.get('page')
  contatos = paginator.get_page(page)
  return render(request, 'pages/busca.html',{
    'contatos': contatos
  })