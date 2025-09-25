from django.db import models

# Create your models here.
# Iniciando o processo para armazenar produtos no banco de dados
class Produto(models.Model):
    PESO_CHOICES = (
        ('LEVE', 'Leve'),
        ('MEDIO', 'Médio'),
        ('PESADO', 'Pesado'),
    )
    
    def __str__(self):
        return self.nome

    # "CharField" para textos curtos,
    nome = models.CharField(max_length=100)
    # "IntegerField" para números inteiros
    quantidade = models.IntegerField()
    peso = models.CharField(max_length=10, choices=PESO_CHOICES, default='LEVE')
    # "DecimalField" para números decimais,
    # "max_digits" é o número total de dígitos
    # "decimal_places" é o número de dígitos após a vírgula
    preco = models.DecimalField(max_digits=10, decimal_places=2)  



