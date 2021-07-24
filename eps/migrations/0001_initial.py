# Generated by Django 3.2.4 on 2021-06-07 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Eps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StockID', models.CharField(default='', max_length=70)),
                ('EPS2021Q1', models.FloatField(default='', max_length=200)),
                ('EPS2020Q4', models.FloatField(default='', max_length=200)),
                ('EPS2020Q3', models.FloatField(default='', max_length=200)),
                ('EPS2020Q2', models.FloatField(default='', max_length=200)),
                ('EPS2020Q1', models.FloatField(default='', max_length=200)),
                ('EPS2019Q4', models.FloatField(default='', max_length=200)),
                ('EPS2019Q3', models.FloatField(default='', max_length=200)),
            ],
        ),
    ]