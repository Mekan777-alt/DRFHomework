from apiip import apiip
from django.conf import settings


def get_country_user(ip_address):

    api_client = apiip(settings.API_CLIENT, {'ssl': True})
    info = api_client.get_location({
        "ip": ip_address,
        "output": "json",
        "fields": "city, countryName",
        "languages": "ru"
    })

    return info
