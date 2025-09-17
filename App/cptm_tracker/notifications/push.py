# Notificações push (exemplo para mobile via Firebase ou OneSignal)
import requests
from django.conf import settings

def enviar_notificacao(usuario, mensagem):
    url = 'https://onesignal.com/api/v1/notifications'
    payload = {
        'app_id': settings.ONESIGNAL_APP_ID,
        'include_external_user_ids': [usuario],
        'contents': {'en': mensagem},
    }
    headers = {
        'Authorization': f'Basic {settings.ONESIGNAL_API_KEY}',
        'Content-Type': 'application/json'
    }
    response = requests.post(url, json=payload, headers=headers, timeout=10)
    return response.json()
