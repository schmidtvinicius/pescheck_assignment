from django.shortcuts import render
from django.http import HttpResponse
from newsapi import NewsApiClient
import requests
import json
from .models import CryptoCurrency

newsapi = NewsApiClient(api_key='3779ffddd95448f6ac0bc70bb87524e5')

CRYPTOS_AVAILABLE = 'cryptos_available.json'

# Create your views here.
def home(request):
    raw_data = open(CRYPTOS_AVAILABLE, 'r')
    crypto_json = json.loads(raw_data.read())
    if not CryptoCurrency.objects.exists():
        for crypto in crypto_json:
            currency = CryptoCurrency()
            currency.name = crypto["name"]
            currency.code = crypto["code"]
            currency.save()
    all_articles = newsapi.get_everything(q='bitcoin')
    return render(request, 'home.html', {
        'top_headlines': CryptoCurrency.objects.all(),
    })