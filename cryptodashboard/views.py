from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.
def home(request):
    url = 'http://newsapi.org/v2/everything?q=bitcoin&from=2020-08-12&sortBy=publishedAt&apiKey=3779ffddd95448f6ac0bc70bb87524e5'
    content = requests.get(url)
    return HttpResponse(f'<p>{content}</p>')