from django.contrib import admin
from django.urls import path

from cryptodashboard import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('crypto-currencies/<str:currency_code>', views.crypto_articles, name='crypto_articles'),
]
