from django.shortcuts import render
from django.http import HttpResponse
from newsapi import NewsApiClient
import requests

api_key='3779ffddd95448f6ac0bc70bb87524e5'

# Create your views here.
def home(request):
    url = (f'http://newsapi.org/v2/everything?q=Bitcoin&sortBy=publishedAt&apiKey={api_key}')
    response = requests.get(url)
    json_object = response.json()
    return HttpResponse(f'<p>{json_object["totalResults"]}</p>')