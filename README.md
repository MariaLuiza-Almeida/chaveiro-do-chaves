# Chaveiro do Chaves 🔑

Breve descrição do projeto e seu propósito.

## Índice

- [Requisitos](#requisitos)
- [Instalação](#instalação)
- [Uso](#uso)
- [Contribuição](#contribuição)
- [Licença](#licença)
- [Contato](#contato)

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