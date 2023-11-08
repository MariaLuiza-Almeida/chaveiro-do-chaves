# Chaveiro do Chaves 🔑

Breve descrição do projeto e seu propósito.

## Índice

- [Requisitos](#requisitos)
- [Get Started](#get-started)
- [Defina Suas Entidades](#defina-suas-entidades)


## Requisitos

### Python

Para instalar o Python é muito simples! Abra o terminal e rode o comando:

```
sudo apt-get install python3.10
```

Após a instalação, verifique a versão com o comando:

```
python3 --version
```

### Django

Após a instalação do Python, seguimos para a instalação do Django. Rode o comando:

```
sudo apt install python3-pip;
pip install Django==4.2.5
```

### Ambiente Virtual 
Para desenvolver seus projetos em django é recomendado utilizar o ambiente virtual da própria ferramenta. Para isso é necessário rodar o comando para instalar:

```
sudo pip install virtualenv
```

Depois disso é necessário criar o ambiente virtual:

```
python3 -m venv nome_do_ambiente
```

Agora todas as vezes que você começar ou retornar a um projeto lembre-se de ativar o ambiente virutal com o comando:

```
source nome_do_ambiente/bin/activate
```
Instale o django dentro do seu ambiente virtual (é necessário instalar ele apenas uma vez):
```
pip install django
```

### Banco de dados

Vamos utilizar o banco de dados que já vem instalado junto com o django, o SQLite.

## Get Started

Agora vamos iniciar um projeto com front-end em Django e back-end em Python.

### Crie uma pasta para armazenar seu projeto

O primeiro passo é selecionar o diretório onde você deseja armazenar seu projeto. Por
exemplo:
- 📂 → workspace
    - 📂 → projetos

### Abra o terminal e acesse o diretório desejado

```
ls
cd workspace
cd projetos
```
###  Rode o comando de iniciar um projeto

```
django-admin startproject chaveiro_do_chaves
```
Este comando criará neste diretório a pasta de seu projeto, resultando em:

- 📂 → workspace
    - 📂 → projetos
        - 📂 → chaveiro_do_chaves

### Acesse a pasta do seu novo projeto

```
ls
cd workspace
cd projetos
cd chaveiro_do_chaves
```

### Verifique se o seu projeto funciona como esperado

```
python manage.py runserver
```

😀 Se tudo estiver certo, você terá como resposta do comando acima a porta na qual
seu projeto roda.
Você pode criar um superusuario para entrar na pagina admin do servidor usando o comando:
```
python manage.py createsuperuser
```


Tudo certo para começar a codar! Como o Django é um framework web de Python, não
é necessário criar projetos separados para back/front-end.

### Configurar o projeto
No vscode abra o arquivo setting.py, procure "INSTALLED_APPS" e coloque o nome do arquivo principal. Todas as vezes que você criar uma nova aplicação no seu projeto você deve adicionar o nome nessa lista. Exemplo:
```
INSTALLED_APPS = [
    # ...
    'chaveiro_do_chaves',
    # ...
]
```
## Crie sua primeira aplicação
```
python manage.py startapp crud
```
Esse comando irá criar uma nova pasta com arquivos como models, views, url, admin e nela vamos criar nossa primeira aplicação que irá nos levar a uma página que vai listar todas as chaves listadas. Lembre-se de colocar o nome da aplicação no "INSTALLED_APPS".

## Defina Suas Entidades

Definir as entidades em uma aplicação Django/Python é muito fácil, siga o passo a passo:

###  Abra o arquivo “models.py”

É onde estarão contidas todas as suas classes

### Utilize o django.db

Este é um pacote do django que contem funcionalidades que auxiliam a definição de
entidades orientadas a banco de dado. Ele traz identificadores como os de primary key,
foreign key e etc, importe ele no começo do código no vscode:

```
from django.db import models
```

### Crie suas classes

Agora é simples, só declarar as classes com seus atributos usando os recursos do
django.db.

Aqui está o código models.py que estará dentro da aplicação:

```
from django.db import models

# Definição da classe
class Chave(models.Model):
    id = models.AutoField(primary_key=True)  # Usando AutoField para a chave primária
    nome = models.CharField(max_length=255, unique=True)  # Defina o valor máximo apropriado para o comprimento do nome
    situacao = models.BooleanField(default=True)  # Campo booleano que indica se está emprestada ou não
    status = models.BooleanField(default=True) # Campo booleano que indica se está disponível para empréstimo
    def __str__(self):
        return self.nome
    
class Servidor(models.Model):
    id = models.AutoField(primary_key=True)  # Usando AutoField para a chave primária
    cpf = models.CharField(max_length=11)  # Defina o valor máximo apropriado para o CPF
    contato = models.CharField(max_length=255)  # Defina o valor máximo apropriado para o contato
    nascimento = models.DateField()
    status = models.BooleanField()

class Emprestimo(models.Model):
    id = models.AutoField(primary_key=True)  # Usando AutoField para a chave primária
    dataHoraEmprestimo = models.DateTimeField()
    dataHoraDevolucao = models.DateTimeField()
    chave = models.ForeignKey(Chave, on_delete=models.CASCADE)  # Adicione o argumento on_delete
    servidorRetirou = models.ForeignKey(Servidor, on_delete=models.CASCADE, related_name='emprestimos_retirados')  # Adicione o argumento on_delete
    servidorDevolveu = models.ForeignKey(Servidor, on_delete=models.CASCADE, related_name='emprestimos_devolvidos')  # Adicione o argumento on_delete     
```

Após criar o models é necessário registrar suas entidades dentro do arquivo admin.py:
```
from .models import Chave, Servidor, Emprestimo
admin.site.register(Chave)
admin.site.register(Servidor)
admin.site.register(Emprestimo)
```
Agora é necessário fazer a migração para o banco usando os seguintes comandos:


```
python manage.py makemigrations
```

Esse comando irá gerar arquivos de migração com base nas classes de modelo já criadas

```
python manage.py migrate
```

Esse comando irá aplicar essas migrações ao banco de dados e criar as tabelas.


### VIEWS
Agora vamos definir a view para listar as páginas disponíveis:

No arquvio views.py dentro da aplicação CRUD importe as entidades necessárias do models, nesse caso usaremmos apenas a Chave:

```
from .models import Chave
```
Crie um request para ir para a página html que será criada:

```
def getKeys (request):
    chaves = Chave.objects.all()
    return render(request, "index.html", {"chaves": chaves})

```

# URLS
Primeiramente vamos mexer no arquivo urls.py do projeto principal.
Faça a importação do include:
```
from django.urls import path, include
```
Dentro do urlpatterns adicione o caminho:
```
urlpatterns = [
    # ... outras URLs
   path('crud/', include('crud.urls')),
]
```
Agora entre no urls.py da sua aplicação crud.
Faça a importação da views:

```
from .views import getKeys
```
Dentro da urlpatterns adicione o caminho:
```
urlpatterns = [
    # ... outras URLs
path('', getKeys, name='getKeys'),
]
```

### Página HTML
Crie uma pasta para os templates dentro da aplicação crud, aqui está um exemplo de código usando ferramentas do python como o "{% for chave in chaves %}" para listar as chaves e o "{% empty %}" para quando a lista estiver vazia.

```
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Listar Chaves</title>
</head>
<body>
<div class="container">
<div class="listKeys">
        <h1>Lista de chaves </h1>
        <u>
            {% for chave in chaves %} 
            <li>{{ chave.nome }}</li>
            {% empty %} 
            <li>Não existe nenhuma chave ainda!</li>
            {% endfor %}
        </u>
    </div>
</u>
</div>

</body>
</html>
```
## TESTE
Para testar vamos abrir o servidor:

```
python manage.py runserver
```
Primeiramente entre no:
```
/crud/
```
Se tudo estiver certo irá aparecer a pagina Listar Chaves com o aviso de que não existe nenhuma chave ainda. Agora para testar se a listagem está funcionando:

Abra o 
```
/admin/
```
Faça o login com o superusuario que foi criado lá em cima. Se tudo estiver correto você vai poder ver o banco de dados e manipular as tabelas, crie algumas chaves e depois volte na página Listar Chaves, agora irá aparecer as chaves que você adicionou na tabela.

## Criar chaves
Agora vamos adicionar a funcionalidade de criar novas chaves, fazendo a validação para não adicionar chaves com nome vazio ou nomes repetidos.

## HTML
Crie um formulário, é necessário adicionar o action e o method que é post
```
<div class="createKey">
<h2>Criar uma nova chave!</h2>
        <div class="forms">
            <form action="{% url 'createKey' %}" method="post">
                {% csrf_token %}
                <h3>Nome:</h3>
                <input type="text" name="nome">
                <button type="submit">Criar</button>
            </form>
        </div>
</div>
```
## VIEWS

Crie um resquest "salvar" no arquivo views.py, nesse resquest já está incluido as verificações e as mensagens de erro para o nome vazio e para o nome repetido:

```
def createKey (request):
    nome = request.POST.get("nome")
    if nome:
        if Chave.objects.filter(nome=nome).exists():
            mensagem_erro = "Nome já existe. Escolha um nome diferente."
        else:
            Chave.objects.create(nome=nome)
            mensagem_erro = None
    else:
        mensagem_erro = "Nome não pode ser vazio."

    chaves = Chave.objects.all()
    return render(request, "index.html", {"chaves": chaves, "mensagem_erro": mensagem_erro})
```

##URLS
Importe "salvar" da views:

```
from .views import getKeys, createKey
```
Dentro do url patterns adicione um novo path:
```
path('createKey/', createKey, name='createKey')

```
#MENSAGEM DE ERRO
Adicione no código html a mensagem de erro para aparecer quando necessário dentro da div 'createKey':

```
    <div class="errorMsg">
            {% if mensagem_erro %}
            <p class="text-danger">{{ mensagem_erro }}</p>
            {% endif %}
    </div>

```

Sua aplicação já está criando novas chaves, adicionando no banco e listando elas no seu template. Agora você já pode estilizar do jeito que você preferir!


