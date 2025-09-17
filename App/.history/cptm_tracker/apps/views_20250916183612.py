from django.shortcuts import render
from .models import Linha, Estacao, Trem

def mapa(request):
    linhas = Linha.objects.all()
    estacoes = Estacao.objects.all()
    trens = Trem.objects.all()
    return render(request, 'mapa.html', {'linhas': linhas, 'estacoes': estacoes, 'trens': trens})
