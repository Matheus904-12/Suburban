# Notificações push (exemplo para mobile via Firebase ou OneSignal)

def enviar_notificacao(usuario, mensagem):
    # Integração real com serviço de push (exemplo: OneSignal)
    import os
    import requests
    onesignal_app_id = os.getenv('ONESIGNAL_APP_ID')
    onesignal_api_key = os.getenv('ONESIGNAL_API_KEY')
    url = 'https://onesignal.com/api/v1/notifications'
    payload = {
        'app_id': onesignal_app_id,
        'include_external_user_ids': [usuario],
        'contents': {'en': mensagem},
    }
    headers = {
        'Authorization': f'Basic {onesignal_api_key}',
        'Content-Type': 'application/json'
    }
    response = requests.post(url, json=payload, headers=headers, timeout=10)
    return response.json()
        from django.conf import settings
        payload = {
            'app_id': settings.ONESIGNAL_APP_ID,
            'include_external_user_ids': [usuario],
            'contents': {'en': mensagem},
        }
        headers = {
            'Authorization': f'Basic {settings.ONESIGNAL_API_KEY}',
            'Content-Type': 'application/json'
        }
