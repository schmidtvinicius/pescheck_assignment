from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from newsapi import NewsApiClient
import requests
import json
from .models import CryptoCurrency
from .management.commands import load_crypto_data

newsapi = NewsApiClient(api_key='3779ffddd95448f6ac0bc70bb87524e5')

# Create your views here.
def home(request):
    if not CryptoCurrency.objects.exists():
        load_crypto_data
    return render(request, 'home.html', {
        'all_currencies': CryptoCurrency.objects.all(),
    })

def crypto_articles(request, currency_code):
    try:
        currency = CryptoCurrency.objects.get(code=currency_code)
    except CryptoCurrency.DoesNotExist:
        raise Http404('Crypto currency not found!')
    top_headlines = newsapi.get_everything(q=currency.name,
                                        language='en')
    return HttpResponse(f'<p>{top_headlines}</p>')
