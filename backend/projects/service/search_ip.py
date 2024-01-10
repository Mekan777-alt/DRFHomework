from apiip import apiip
from django.conf import settings
import requests


def get_country_user(ip_address):

    api_client = apiip(settings.API_CLIENT)
    info = api_client.get_location({
        "ip": ip_address,
        "output": "json",
        "fields": "countryName",
        "languages": "ru"
    })

    return info
