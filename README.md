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

### MySQL

Por fim, vamos instalar o banco de dados (no nosso caso, o MySQL):

```
sudo apt update
sudo apt install mysql-server
sudo systemctl start mysql.service
```

Após a instalção, configure seu usuário no banco:

```
sudo mysql
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '${digite_sua_senha}';
exit
```

Após a instalação, verifique se está tudo certo

```
systemctl status mysql.service
```

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

Tudo certo para começar a codar! Como o Django é um framework web de Python, não
é necessário criar projetos separados para back/front-end.

## Defina Suas Entidades

Definir as entidades em uma aplicação Django/Python é muito fácil, siga o passo a passo:

###  Crie um arquivo “models.py”

É onde estarão contidas todas as suas classes

### Utilize o django.db

Este é um pacote do django que contem funcionalidades que auxiliam a definição de
entidades orientadas a banco de dado. Ele traz identificadores como os de primary key,
foreign key e etc

```
from django.db import models
```

### Crie suas classes

Agora é simples, só declarar as classes com seus atributos usando os recursos do
django.db. Segue um exemplo da classe chave:

`Atributos: id, nome, situação, status`

```
# Definição da classe
class Chave(models.Model):
id = models.IntegerField(primary_key=True) #Declarando um campo inteiro que é chave primária
nome = models.CharField(min=3) #Nome com mínimo de caracteres
situacao = models.BooleanField() #Campo booleano que indica se está emprestada ou não
status = models.BooleanField() #Campo booleano que indica se está disponível para empréstimo
```

🥸 Agora é só aplicar para as outras entidades. Para saber os tipos de campos disponíveis
no django.db, acesse:

[DJANGO](https://docs.djangoproject.com/en/4.2/topics/db/models/)

PARTE 4
Crie um documento descrevendo como criar o BD do seu sistema para armazenar os dados das entidades do sistema (Chave, Servidor, Emprestimo) usando as tecnologias do seu grupo.

1- PASSO 
CONECTAR O BANCO DE DADOS 

Instalar o pacote python para banco de dados

pip install mysql-connector-python

Utilize a biblioteca mysql.connector:

import mysql.connector db = mysql.connector.connect( host=”localhost”, user=”your_username”, password=”your_password”, database=”your_database”)


2- PASSO
Executar os seguintes comandos: 

python manage.py makemigrations

Esse comando irá gerar arquivos de migração com base nas classes de modelo já criadas


python manage.py migrate

Esse comando irá aplicar essas migrações ao banco de dados e criar as tabelas.

PARTE 5
Crie um documento descrevendo como criar a funcionalidade "listar chaves disponíveis" incluindo o frontend e o backend usando as tecnologias do seu grupo.


1- PASSO
Definir VIEW para listar chaves disponíveis: 

# views.py

from django.shortcuts import render
from .models import Chave

def listar_chaves_disponiveis(request):
    chaves_disponiveis = Chave.objects.filter(situacao=False)  # Filtra as chaves que não estão emprestadas
    return render(request, 'emprestimos_chaves/listar_chaves_disponiveis.html', {'chaves_disponiveis': chaves_disponiveis})

2- PASSO
Configurar a URL

# urls.py

from django.urls import path
from . import views

urlpatterns = [
    # ... outras URLs
    path('chaves/disponiveis/', views.listar_chaves_disponiveis, name='listar_chaves_disponiveis'),
]

3- PASSO
Criar um arquivo html 

Exemplo:

<!DOCTYPE html>
<html>
<head>
    <title>Chaves Disponíveis</title>
</head>
<body>
    <h1>Chaves Disponíveis</h1>
    <ul>
        {% for chave in chaves_disponiveis %}
            <li>{{ chave.nome }}</li>
        {% empty %}
            <li>Nenhuma chave disponível no momento.</li>
        {% endfor %}
    </ul>
</body>
</html>

PARTE 6

1- PASSO
Definir a view para adicionar uma nova chave:

 # views.py

from django.shortcuts import render, redirect
from .models import Chave
from .forms import ChaveForm

def adicionar_chave(request):
    if request.method == 'POST':
        form = ChaveForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_chaves_disponiveis')
    else:
        form = ChaveForm()
    return render(request, 'emprestimos_chaves/adicionar_chave.html', {'form': form})



2- PASSO
Criar um formulário para adicionar as novas chaves:

# forms.py

from django import forms
from .models import Chave

class ChaveForm(forms.ModelForm):
    class Meta:
        model = Chave
        fields = ['nome', 'situacao', 'status']

3- PASSO
Configurar a URL para acessar a visualização de adicionar a nova chave:

# urls.py

from django.urls import path
from . import views

urlpatterns = [
    # ... outras URLs
    path('chaves/adicionar/', views.adicionar_chave, name='adicionar_chave'),
]


4- PASSO
Criar uma página html que irá aparecer o formulário para adicionar uma nova chave:

<!DOCTYPE html>
<html>
<head>
    <title>Adicionar Chave</title>
</head>
<body>
    <h1>Adicionar Nova Chave</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Salvar</button>
    </form>
</body>
</html>



