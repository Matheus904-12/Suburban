
from django.shortcuts import render
from django.http import JsonResponse
from .models import Linha, Estacao, Trem

def mapa(request):
    linhas = Linha.objects.prefetch_related('estacoes', 'trens').all()
    estacoes = Estacao.objects.all()
    trens = Trem.objects.select_related('linha', 'estacao_atual').all()
    return render(request, 'mapa.html', {
        'linhas': linhas,
        'estacoes': estacoes,
        'trens': trens
    })

def api_trens(request):
    trens = Trem.objects.select_related('linha', 'estacao_atual').all()
    data = [
        {
            'identificador': trem.identificador,
            'linha': trem.linha.nome,
            'lotacao': trem.lotacao,
            'status': trem.status,
            'ultima_atualizacao': trem.ultima_atualizacao,
            'estacao_atual': trem.estacao_atual.nome if trem.estacao_atual else None
        }
        for trem in trens
    ]
    return JsonResponse({'trens': data})
