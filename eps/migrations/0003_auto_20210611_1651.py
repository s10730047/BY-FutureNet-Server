# Generated by Django 3.2.4 on 2021-06-11 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eps', '0002_auto_20210609_2025'),
    ]

    operations = [
        migrations.AddField(
            model_name='eps',
            name='EPS2019Q1',
            field=models.FloatField(blank=True, default='0', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='eps',
            name='EPS2019Q2',
            field=models.FloatField(blank=True, default='0', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='eps',
            name='EPS2019Q3',
            field=models.FloatField(blank=True, default='0', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='eps',
            name='EPS2019Q4',
            field=models.FloatField(blank=True, default='0', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='eps',
            name='EPS2020Q1',
            field=models.FloatField(blank=True, default='0', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='eps',
            name='EPS2020Q2',
            field=models.FloatField(blank=True, default='0', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='eps',
            name='EPS2020Q3',
            field=models.FloatField(blank=True, default='0', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='eps',
            name='EPS2020Q4',
            field=models.FloatField(blank=True, default='0', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='eps',
            name='EPS2021Q1',
            field=models.FloatField(blank=True, default='0', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='eps',
            name='StockID',
            field=models.CharField(blank=True, default='', max_length=70, null=True),
        ),
    ]
