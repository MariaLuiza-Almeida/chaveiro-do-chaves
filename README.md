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
Para desenvolver seus projetos em django é recomendado utilizar o ambiente virtual da própria ferramenta. Para isso é necessário rodar o comando o para criar ela:

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
python manage.py startapp listarChaves
```
Esse comando irá criar uma nova pasta com arquivos como models, views, url, admin e nela vamos criar nossa primeira aplicação que irá nos levar a uma página que vai listar todas as chaves listadas.

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

Aqui está o código models.py que estará dentro da aplicação listarChaves:

```
from django.db import models

# Definição da classe
class Chave(models.Model):
    id = models.AutoField(primary_key=True)  # Usando AutoField para a chave primária
    nome = models.CharField(max_length=255)  # Defina o valor máximo apropriado para o comprimento do nome
    situacao = models.BooleanField()  # Campo booleano que indica se está emprestada ou não
    status = models.BooleanField()  # Campo booleano que indica se está disponível para empréstimo
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

No arquvio views.py dentro da aplicação listarChaves importe as entidades necessárias do models, nesse caso usaremmos apenas a Chave:

```
from .models import Chave
```
Crie um request para ir para a página html que será criada:

```
def home(request):
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
   path('listarChaves/', include('listarChaves.urls')),
]
```
Agora entre no urls.py da sua aplicação listarChaves.
Faça a importação da views:

```
from .views import home
```
Dentro da urlpatterns adicione o caminho:
```
urlpatterns = [
    # ... outras URLs
path('', home, name='home'),
]
```

### Página HTML
Crie uma pasta para os templates, ela pode ser criada na pasta do projeto principal fora da aplicação.

```
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Listar Chaves</title>
</head>
<body>
<h1>Lista de chaves </h1>
<u>
    {% for chave in chaves %} ## comando do python que serve para listar as chaves
    <li>{{ chave.nome }}</li>
    {% empty %} ## comando do python para quando a lista estiver vazia
    <li>Não existe nenhuma chave ainda!</li>
    {% endfor %}
</u>

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
/listarChaves/
```
Se tudo estiver certo irá aparecer a pagina Listar Chaves com o aviso de que não existe nenhuma chave ainda. Agora para testar se a listagem está funcionando:

Abra o 
```
/admin/
```
Faça o login com o superusuario que foi criado lá em cima. Se tudo estiver correto você vai poder ver o banco de dados e manipular as tabelas, crie algumas chaves e depois volte na página Listar Chaves, agora irá aparecer as chaves que você adicionou na tabela.

## Adicionar chaves


