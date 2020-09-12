from django.shortcuts import render
from django.http import HttpResponse
from newsapi import NewsApiClient
import requests

newsapi = NewsApiClient(api_key='3779ffddd95448f6ac0bc70bb87524e5')

# Create your views here.
def home(request):
    url = ('http://newsapi.org/v2/everything?q=bitcoin&from=2020-08-12&sortBy=publishedAt&apiKey=3779ffddd95448f6ac0bc70bb87524e5')
    response = requests.get(url)
    print(response.json())
    return HttpResponse(f'<p>{response.json()}</p>')