# Generated by Django 3.0.3 on 2020-09-14 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cryptodashboard', '0003_auto_20200913_1905'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='published_at',
            field=models.DateField(null=True),
        ),
    ]