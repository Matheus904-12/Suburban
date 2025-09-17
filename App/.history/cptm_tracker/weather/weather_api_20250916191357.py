# Integração com OpenWeatherMap (gratuita)
import requests
from django.conf import settings

def buscar_clima(lat, lon):
    api_key = settings.OPENWEATHER_API_KEY
    url = f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={api_key}&units=metric&lang=pt_br'
    response = requests.get(url, timeout=10)
    if response.status_code == 200:
        return response.json()
    return None
