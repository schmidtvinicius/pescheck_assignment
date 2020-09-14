from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from newsapi import NewsApiClient
import requests
import json
from .models import CryptoCurrency, Article
from .management.commands.load_crypto_data import load_crypto_currencies
from .management.commands.load_articles import load_articles

newsapi = NewsApiClient(api_key='3779ffddd95448f6ac0bc70bb87524e5')

# Create your views here.
def home(request):
    #Article.objects.all().delete()
    if not CryptoCurrency.objects.exists():
        load_crypto_currencies()
    return render(request, 'home.html', {
        'all_currencies': CryptoCurrency.objects.all(),
    })

def currency_articles(request, currency_code='BTC'):
    try:
        currency = CryptoCurrency.objects.get(code=currency_code)
    except CryptoCurrency.DoesNotExist:
        raise Http404('Crypto currency not found!')
    if(not Article.objects.exists()):
        load_articles()
    all_articles = Article.objects.all()
    matching_articles = []
    for article in all_articles:
        currencies_discussed = article.currencies_discussed.all()
        if currencies_discussed.get(name=currency.name) != None:
            matching_articles.append(article)
    return render(request, 'currency_articles.html', {
        'articles': matching_articles, 
    })
