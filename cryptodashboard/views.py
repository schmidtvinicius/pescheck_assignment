from django.shortcuts import render
from django.http import HttpResponse
from newsapi import NewsApiClient
import requests
from .models import CryptoCurrency

newsapi = NewsApiClient(api_key='3779ffddd95448f6ac0bc70bb87524e5')

# Create your views here.
def home(request):
    all_articles = newsapi.get_everything(q='bitcoin')
    return render(request, 'home.html', {
        'top_headlines': CryptoCurrency.objects.all(),
    })