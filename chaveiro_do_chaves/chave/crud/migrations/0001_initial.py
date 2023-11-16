# Generated by Django 4.2.7 on 2023-11-07 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chave',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
                ('situacao', models.BooleanField()),
                ('status', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Servidor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cpf', models.CharField(max_length=11)),
                ('contato', models.CharField(max_length=255)),
                ('nascimento', models.DateField()),
                ('status', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Emprestimo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('dataHoraEmprestimo', models.DateTimeField()),
                ('dataHoraDevolucao', models.DateTimeField()),
                ('chave', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud.chave')),
                ('servidorDevolveu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emprestimos_devolvidos', to='crud.servidor')),
                ('servidorRetirou', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emprestimos_retirados', to='crud.servidor')),
            ],
        ),
    ]