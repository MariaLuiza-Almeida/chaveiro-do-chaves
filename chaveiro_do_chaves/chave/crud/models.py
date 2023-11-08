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