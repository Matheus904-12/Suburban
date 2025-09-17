
# Integração com Direto dos Trens (gratuita)
import requests

def buscar_status_linhas():
    url = 'https://www.diretodostrens.com.br/api/status'
    response = requests.get(url, timeout=10)
    if response.status_code == 200:
        return response.json()
    return None

def buscar_status_linha(linha):
    url = f'https://www.diretodostrens.com.br/api/status/codigo/{linha}'
    response = requests.get(url, timeout=10)
    if response.status_code == 200:
        return response.json()
    return None

def buscar_detalhe_status(id_status):
    url = f'https://www.diretodostrens.com.br/api/status/id/{id_status}'
    response = requests.get(url, timeout=10)
    if response.status_code == 200:
        return response.json()
    return None
