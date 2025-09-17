# Integração com OpenWeatherMap
import requests


def buscar_clima(lat, lon):
    import os
    api_key = os.getenv('OPENWEATHER_API_KEY')
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&lang=pt_br&units=metric'
    response = requests.get(url, timeout=10)
    if response.status_code == 200:
        return response.json()
    return None
        from django.conf import settings
        api_key = settings.OPENWEATHER_API_KEY
        url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&lang=pt_br&units=metric'
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.json()
        return None
