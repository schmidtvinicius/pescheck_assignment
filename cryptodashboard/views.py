from django.shortcuts import render
from django.http import HttpResponse
from newsapi import NewsApiClient
import requests

api_key='3779ffddd95448f6ac0bc70bb87524e5'

# Create your views here.
def home(request):
    url = (f'http://newsapi.org/v2/sources?q=crypto&sortBy=publishedAt&apiKey={api_key}')
    response = requests.get(url)
    json_object = response.json()
    sources_list = json_object["sources"]
    # for article in json_object["sources"]:
    #     short_article = {
    #         "source": article["source"],
    #         "author": article["author"],
    #         "title": article["title"],
    #         "url": article["url"],
    #         "description": article["description"]
    #     }
    #     articles_list.append(short_article)
    return HttpResponse(f'<p>currently showing{len(sources_list)}articles</p><p>{sources_list}</p>')