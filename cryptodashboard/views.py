from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.http import HttpResponseBadRequest
from newsapi import NewsApiClient
from pytz import UTC
from datetime import datetime
import re
import requests
import json
from .models import CryptoCurrency, Article
from .management.commands.load_crypto_data import load_crypto_currencies
from .management.commands.load_articles import load_articles

newsapi = NewsApiClient(api_key='3779ffddd95448f6ac0bc70bb87524e5')

date_pattern = re.compile('^[0-9]{4}-[01][1-9]-[01][1-9]$')

ORDER_BY_OPTIONS = {
    'Oldest': 'published_at', 
    'Newest': '-published_at', 
    'Alphabetical': 'title'
}

DATE_FORMAT = '%Y-%m-%d'

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

    if(not Article.objects.exists()):
        load_articles()

    order_by = request.GET.get('order-by')
    filter_domain = request.GET.get('filter-domain')
    if filter_domain == None:
        filter_domain = ''
    # if str(filter_date) != '' and not date_pattern.match(str(filter_date)):
    #     return HttpResponseBadRequest('Given date is invalid')
    
    if order_by == None:
        order_by = 'Newest'
    
    if filter_domain == '':
        all_articles = Article.objects.all().order_by(ORDER_BY_OPTIONS[order_by])
    else: 
        all_articles = Article.objects.filter(url__contains=filter_domain).order_by(ORDER_BY_OPTIONS[order_by])
    
    domains = []
    matching_articles = []
    for article in all_articles:
        try:
            matching_currency = article.currencies_discussed.get(name=currency.name)
            matching_articles.append(article)
            split_url = article.url.split('/')
            if not split_url[2] in domains:
                domains.append(split_url[2])
        except CryptoCurrency.DoesNotExist:
            matching_currency = None
    return render(request, 'currency_articles.html', {
        'articles': matching_articles,
        'domains': domains,
        'order_by_options': ORDER_BY_OPTIONS.keys,
    })
