# Integração com OpenWeatherMap
import requests

def buscar_clima(lat, lon):
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=SUA_API_KEY&lang=pt_br&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None
