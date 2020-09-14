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

ORDER_BY_OPTIONS = ('Oldest', 'Newest', 'Alphabetical')

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
    order_by = request.GET.get('order-by')
    filter_date = request.GET.get('filter-date')
    if filter_date == None:
        filter_date = ''
    else:
        filter_date = UTC.localize(datetime.strptime(filter_date, DATE_FORMAT))
    if str(filter_date) != '' and not date_pattern.match(str(filter_date)):
        return HttpResponseBadRequest('Given date is invalid')
    if order_by == None:
        order_by = ORDER_BY_OPTIONS[ORDER_BY_OPTIONS.index('Newest')]
    if(not Article.objects.exists()):
        load_articles()
    if order_by == ORDER_BY_OPTIONS[0]:
        all_articles = Article.objects.filter(published_at=filter_date).order_by('published_at')
    elif order_by == ORDER_BY_OPTIONS[1]:
        all_articles = Article.objects.filter(published_at=filter_date).order_by('-published_at')
    elif order_by == ORDER_BY_OPTIONS[2]:
        all_articles = Article.objects.filter(published_at=filter_date).order_by('title')
    else:
        return HttpResponseBadRequest(f'Cannot order by {order_by}')
    dates = []
    matching_articles = []
    for article in all_articles:
        try:
            matching_currency = article.currencies_discussed.get(name=currency.name)
            matching_articles.append(article)
            dates.append(article.published_at)
        except CryptoCurrency.DoesNotExist:
            matching_currency = None
    return render(request, 'currency_articles.html', {
        'articles': matching_articles,
        'dates': dates,
        'order_by_options': ORDER_BY_OPTIONS,
    })
