from django.db import models

# Create your models here.
class CryptoCurrency(models.Model):
    name = models.CharField(max_length=25)
    code = models.CharField(max_length=3)

    def __str__(self):
        return f'{self.name} ({self.code})'

class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=25)
    description = models.TextField(blank=False)
    url = models.TextField(blank=False)
    currencies_discussed = models.ManyToManyField('CryptoCurrency', blank=False)



