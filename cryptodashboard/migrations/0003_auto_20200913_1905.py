# Generated by Django 3.0.3 on 2020-09-13 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cryptodashboard', '0002_auto_20200913_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.TextField(),
        ),
    ]
