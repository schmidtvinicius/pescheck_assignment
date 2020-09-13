from django.contrib import admin

from .models import CryptoCurrency

# Register your models here.
@admin.register(CryptoCurrency)
class CryptoCurrencyAdmin(admin.ModelAdmin):
    list_display = ['name', 'code']