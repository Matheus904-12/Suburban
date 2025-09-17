# Integração com mapas gratuitos
import requests

# OpenStreetMap via Nominatim (gratuito)
def buscar_trajetoria_trem_osm(origem, destino):
    # Exemplo: busca coordenadas de origem e destino
    url_origem = f'https://nominatim.openstreetmap.org/search?q={origem}&format=json'
    url_destino = f'https://nominatim.openstreetmap.org/search?q={destino}&format=json'
    resp_origem = requests.get(url_origem, headers={'User-Agent': 'CPTMTracker/1.0'}, timeout=10)
    resp_destino = requests.get(url_destino, headers={'User-Agent': 'CPTMTracker/1.0'}, timeout=10)
    if resp_origem.status_code == 200 and resp_destino.status_code == 200:
        data_origem = resp_origem.json()
        data_destino = resp_destino.json()
        if data_origem and data_destino:
            return {
                'origem': data_origem[0],
                'destino': data_destino[0]
            }
    return None
