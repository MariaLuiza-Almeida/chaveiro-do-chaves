from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from .models import Chave


# Create your views here.
def menu (request):
    chaves = Chave.objects.all()
    return render(request, "index.html", {"chaves": chaves})

def getKeys (request):
    chaves = Chave.objects.all()
    return render(request, "getKeys.html", {"chaves": chaves})

def getKeysByName(request):
    # Defina o key name, que é o que será passado para o método através de um formulário.
    keyName = request.GET.get("keyName")

    # Defina chave, que será responsável por receber o retorno da busca pela chave
    chave = None
    
    # Faremos um try/except caso keyName tenha valores. Ou seja, caso não seja o first render da página
    if keyName:
            try:
                # Buscamos a key pelo nome e retornamos para o nossa página
                chave = Chave.objects.get(nome=keyName)
                return render(request, "getKeysByName.html", {"chave": chave})
                # Caso haja uma exceção, renderizamos nossa página com a cahve nula
            except Chave.DoesNotExist:
                return render(request, "getKeysByName.html", {"chave": chave})
                # O mesmo acontece com o default
    return render(request, "getKeysByName.html", {"chave": chave})


def createKey(request):
    nome = request.POST.get("nome")
    mensagem_erro = None
    mensagem_sucesso = None

    if request.method == "POST":
        if nome:
            if Chave.objects.filter(nome=nome).exists():
                mensagem_erro = "Nome já existe. Escolha um nome diferente."
            else:
                Chave.objects.create(nome=nome)
                mensagem_sucesso = f"Chave '{nome}' criada com sucesso!"
                nome = ""  # Limpar o campo de nome após o sucesso
        else:
            mensagem_erro = "Nome não pode ser vazio."

    chaves = Chave.objects.all()
    return render(request, "createKey.html", {"chaves": chaves, "mensagem_erro": mensagem_erro, "mensagem_sucesso": mensagem_sucesso})

def editKeys(request):
    chaves = Chave.objects.all()
    return render(request, "editKeys.html", {"chaves": chaves})

def updateKey (request, id):
    chaves = Chave.objects.get(id=id)
    return render (request, "update.html", {"chaves": chaves})

def update(request, id):
    novoNome = request.POST.get("nome")
    chaves = Chave.objects.get(id=id)
    chaves.nome = novoNome
    chaves.save()
    return redirect (menu)

def delete (request, id):
    # buscamos a chave
    chave = Chave.objects.get(id=id)
    # setamos o status como 0
    chave.status = 0
    # salvamos
    chave.save()
    return redirect (menu)
