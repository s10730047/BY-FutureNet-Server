# Generated by Django 3.2.4 on 2021-06-26 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Futures', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='future',
            name='Date',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='future',
            name='Fluctuation',
            field=models.CharField(blank=True, default='0', max_length=50, null=True),
        ),
    ]
