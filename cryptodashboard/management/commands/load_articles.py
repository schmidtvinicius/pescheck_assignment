from newsapi import NewsApiClient
from cryptodashboard.models import CryptoCurrency, Article
from django.core.management import BaseCommand
from .load_crypto_data import load_crypto_currencies
from pytz import UTC
from datetime import datetime

newsapi = NewsApiClient(api_key='3779ffddd95448f6ac0bc70bb87524e5')

DATETIME_FORMAT = '%Y-%m-%d'

TODAY = datetime.today().strftime('%Y-%m-%d')

def load_articles():
    if not CryptoCurrency.objects.exists():
        load_crypto_currencies()
    all_currencies = CryptoCurrency.objects.all()
    all_urls = []
    for currency in all_currencies:
        top_headlines = newsapi.get_everything(q=f'crypto AND {currency.name}', page_size=100)
        all_articles = top_headlines["articles"]
        for tmp_article in all_articles:
            if not tmp_article["url"] in all_urls:
                all_urls.append(tmp_article["url"])
                published_at = tmp_article["publishedAt"]
                published_at = published_at.split('T', 1)
                published_at = UTC.localize(datetime.strptime(published_at[0], DATETIME_FORMAT))
                article = Article(title=tmp_article["title"], 
                                    author=tmp_article["author"], 
                                    description=tmp_article["description"], 
                                    url=tmp_article["url"], 
                                    published_at=published_at)
                article.save()
                article.currencies_discussed.add(currency)
            else:
                Article.objects.get(url=tmp_article["url"]).currencies_discussed.add(currency)

def update_articles():
    
    if not Article.objects.exists():
        load_articles
    
    urls = load_todays_urls

    todays_saved_articles = Article.objects.filter(published_at=TODAY)
    all_currencies = CryptoCurrency.objects.all()
    for currency in all_currencies:
        everything = newsapi.get_everything(q=f'crypto AND {currency.name}', page_size=100, from_param=TODAY)
        todays_articles = everything["articles"]
        for todays_article in todays_articles:
            if not todays_article["url"] in urls:
                new_article = Article(title=tmp_article["title"], 
                                    author=tmp_article["author"], 
                                    description=tmp_article["description"], 
                                    url=tmp_article["url"], 
                                    published_at=published_at)
                new_article.save()
                new_article.currencies_discussed.add(currency)
            else:
                existing_article = Article.objects.get(url=todays_article["url"])
                currencies_discussed = existing_article.currencies_discussed.all()
                contains_currency = False
                for currency_discussed in currencies_discussed:
                    if currency.code == currency_discussed.code:
                        contains_currency = True
                Article.objects.get(url=todays_article["url"]).currencies_discussed.add(currencies_discussed) if contains_currency == False
        
    saved_articles = Article.objects.filter(published_at=TODAY)

def load_todays_urls():
    todays_articles = Article.objects.filter(published_at=TODAY)
    urls = []
    for todays_article in todays_articles:
        urls.append(todays_article.url)

    return urls