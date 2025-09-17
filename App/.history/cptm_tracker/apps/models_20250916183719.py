from django.db import models

class Linha(models.Model):
    nome = models.CharField(max_length=100)
    cor = models.CharField(max_length=20)

class Estacao(models.Model):
    nome = models.CharField(max_length=100)
    linha = models.ForeignKey(Linha, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()

class Trem(models.Model):
    identificador = models.CharField(max_length=50)
    linha = models.ForeignKey(Linha, on_delete=models.CASCADE)
    lotacao = models.IntegerField()
    status = models.CharField(max_length=50)
    ultima_atualizacao = models.DateTimeField(auto_now=True)
