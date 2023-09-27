from django.db import models


# Definição da classe
class Chave(models.Model):
    id = models.IntegerField(primary_key=True) #Declarando um campo inteiro que é chave primária
    nome = models.CharField(min=3) #Nome com mínimo de caracteres
    situacao = models.BooleanField() #Campo booleano que indica se está emprestada ou não
    status = models.BooleanField() #Campo booleano que indica se está disponível para empréstimo

class Servidor(models.Model):
    id = models.IntegerField(primary_key=True)
    cpf = models.CharField(min=11)
    contato = models.CharField()
    nascimento = models.DateField()
    status = models.BooleanField()


class Emprestimo(models.Model):
    id = models.IntegerField(primary_key=True)
    dataHoraEmprestimo: models.DateTimeField()
    dataHoraDevolucao: models.DateTimeField()
    chave: models.ForeignKey(Chave)
    servidorRetirou: models.ForeignKey(Servidor)
    servidorDevolveu: models.ForeignKey(Servidor)
