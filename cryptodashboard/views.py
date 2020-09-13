from django.shortcuts import render
from django.http import HttpResponse
from newsapi import NewsApiClient
import requests

newsapi = NewsApiClient(api_key='3779ffddd95448f6ac0bc70bb87524e5')

# Create your views here.
def home(request):
    top_headlines = newsapi.get_top_headlines(q='bitcoin', sources='bbc-news')
    return render(request, 'home.html', {
        'top_headlines': top_headlines,
    })