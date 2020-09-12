from django.shortcuts import render
from django.http import HttpResponse
from newsapi import NewsApiClient
import requests

api_key='3779ffddd95448f6ac0bc70bb87524e5'

# Create your views here.
def home(request):
    url = (f'http://newsapi.org/v2/everything?q=crypto&sortBy=publishedAt&apiKey={api_key}')
    response = requests.get(url)
    return HttpResponse(f'<p>{len(response.json())}</p>')