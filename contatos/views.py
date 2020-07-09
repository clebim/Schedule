from django.shortcuts import render
from .models import Contato

# Create your views here.

def index(request):
  contatos = Contato.objects.all()
  return render(request, 'pages/index.html',{
    'contatos': contatos
  })


def store(request, id):
  contato = Contato.objects.get(id=id)
  return render(request, 'pages/store.html',{
    'contato': contato
  })