# Integração com a API da CPTM
import requests

def buscar_status_trens():
    # Exemplo de endpoint fictício
    url = 'https://api.cptm.sp.gov.br/v1/trens/status'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None
