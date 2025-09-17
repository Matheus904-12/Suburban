# Integração com Google Maps
import requests


def buscar_trajetoria_trem(origem, destino):
    # Use variáveis de ambiente para a chave
    import os
    api_key = os.getenv('GOOGLE_MAPS_API_KEY')
    url = f'https://maps.googleapis.com/maps/api/directions/json?origin={origem}&destination={destino}&key={api_key}'
    response = requests.get(url, timeout=10)
    if response.status_code == 200:
        return response.json()
    return None
        from django.conf import settings
        api_key = settings.GOOGLE_MAPS_API_KEY
        url = f'https://maps.googleapis.com/maps/api/directions/json?origin={origem}&destination={destino}&key={api_key}'
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.json()
        return None
