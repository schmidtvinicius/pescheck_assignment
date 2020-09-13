from newsapi import NewsApiClient
from cryptodashboard.models import CryptoCurrency, Article
from django.core.management import BaseCommand
import load_crypto_data

newsapi = NewsApiClient(api_key='3779ffddd95448f6ac0bc70bb87524e5')

class Command(BaseCommand):
    if(not CryptoCurrency.objects.exists()):
        load_crypto_data
    all_currencies = CryptoCurrency.objects.all()
    for currency in all_currencies:
        top_headlines = newsapi.get_everything(q=f'crypto AND {currency.name}', page_size=100)
        all_articles = top_headlines['articles']
        for tmp_article in all_articles:
            article = Article(title=tmp_article['title'], author=tmp_article['author'], description=tmp_article['description'], url=tmp_article['url'])
            article_body = tmp_article['content']
            for currency_topic in all_currencies:
                if currency_topic in article_body:
                    article.currencies_discussed.add(currency_topic.name)
            article.save()