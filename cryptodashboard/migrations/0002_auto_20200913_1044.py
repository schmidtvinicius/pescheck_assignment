# Generated by Django 3.0.3 on 2020-09-13 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cryptodashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cryptocurrency',
            name='code',
            field=models.CharField(max_length=10),
        ),
    ]