# Integração com a API da CPTM
import requests
from django.conf import settings

def buscar_status_trens():
    url = 'https://api.cptm.sp.gov.br/v1/trens/status'  # Verifique documentação oficial
    headers = {
        'Authorization': f'Bearer {settings.CPTM_API_TOKEN}',
        'Accept': 'application/json'
    }
    response = requests.get(url, headers=headers, timeout=10)
    if response.status_code == 200:
        return response.json()
    return None
