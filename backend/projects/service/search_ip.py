from apiip import apiip
from django.conf import settings
import requests


def get_country_user(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    api_client = apiip(settings.API_CLIENT)
    info = api_client.get_location({
            "ip": ip,
            "output": "json",
            "fields": "countryName",
            "languages": "en"
    })

    return info.get('countryName', None) if info else None
