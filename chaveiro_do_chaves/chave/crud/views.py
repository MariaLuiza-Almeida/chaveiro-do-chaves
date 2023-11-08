from django.shortcuts import render
from .models import Chave


# Create your views here.
def getKeys (request):
    chaves = Chave.objects.all()
    return render(request, "index.html", {"chaves": chaves})

def createKey (request):
    nome = request.POST.get("nome")
    if nome:
        if Chave.objects.filter(nome=nome).exists():
            # Nome já existe, retorne uma mensagem de erro
            mensagem_erro = "Nome já existe. Escolha um nome diferente."
        else:
            Chave.objects.create(nome=nome)
            mensagem_erro = None
    else:
        mensagem_erro = "Nome não pode ser vazio."

    chaves = Chave.objects.all()
    return render(request, "index.html", {"chaves": chaves, "mensagem_erro": mensagem_erro})