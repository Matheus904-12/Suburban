# Integração com Google Maps
import requests

def buscar_trajetoria_trem(origem, destino):
    # Exemplo de uso da API Directions
    url = f'https://maps.googleapis.com/maps/api/directions/json?origin={origem}&destination={destino}&key=SUA_API_KEY'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None
