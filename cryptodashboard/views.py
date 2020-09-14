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

ORDER_BY_OPTIONS = ('Oldest', 'Newest', 'Alphabetical')

# Create your views here.
def home(request):
    #Article.objects.all().delete()
    if not CryptoCurrency.objects.exists():
        load_crypto_currencies()
    return render(request, 'home.html', {
        'all_currencies': CryptoCurrency.objects.all(),
    })

def currency_articles(request, currency_code):
    try:
        currency = CryptoCurrency.objects.get(code=currency_code)
    except CryptoCurrency.DoesNotExist:
        raise Http404('Crypto currency not found!')
    order_by = request.GET.get('order-by')
    if order_by == None:
        order_by = ORDER_BY_OPTIONS[ORDER_BY_OPTIONS.index('Newest')]
    if(not Article.objects.exists()):
        load_articles()
    all_articles = Article.objects.all().order_by()
    matching_articles = []
    for article in all_articles:
        try:
            matching_currency = article.currencies_discussed.get(name=currency.name)
            matching_articles.append(article)
        except CryptoCurrency.DoesNotExist:
            matching_currency = None
    return render(request, 'currency_articles.html', {
        'articles': matching_articles,
        'order_by_options': ORDER_BY_OPTIONS,
    })
