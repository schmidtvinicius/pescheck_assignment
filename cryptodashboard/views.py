from django.shortcuts import render
from django.http import HttpResponse
from newsapi import NewsApiClient
import requests
import json
from .models import CryptoCurrency
import management.commands.load_crypto_data

newsapi = NewsApiClient(api_key='3779ffddd95448f6ac0bc70bb87524e5')

# Create your views here.
def home(request):
    if not CryptoCurrency.objects.exists():
        management.commands.load_crypto_data
    return render(request, 'home.html', {
        'all_currencies': CryptoCurrency.objects.all(),
    })