# Generated by Django 3.2.4 on 2021-06-26 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Future',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField(blank=True, default='', max_length=50, null=True)),
                ('TAIEX', models.FloatField(blank=True, default='0', max_length=50, null=True)),
                ('Fluctuation', models.FloatField(blank=True, default='0', max_length=50, null=True)),
                ('ForeignInvestors', models.FloatField(blank=True, default='0', max_length=50, null=True)),
                ('InvestmentTrust', models.FloatField(blank=True, default='0', max_length=50, null=True)),
                ('Dealer', models.FloatField(blank=True, default='0', max_length=50, null=True)),
                ('Margin', models.FloatField(blank=True, default='0', max_length=50, null=True)),
                ('MarginChange', models.FloatField(blank=True, default='0', max_length=50, null=True)),
                ('ShortSelling', models.FloatField(blank=True, default='0', max_length=50, null=True)),
                ('ShortSellingChang', models.FloatField(blank=True, default='0', max_length=50, null=True)),
                ('FuturesLongOpenPosition', models.IntegerField(blank=True, default='0', max_length=50, null=True)),
                ('FuturesShortOpenPosition', models.IntegerField(blank=True, default='0', max_length=50, null=True)),
                ('FuturesNet', models.IntegerField(blank=True, default='0', max_length=50, null=True)),
                ('FuturesLongVary', models.IntegerField(blank=True, default='0', max_length=50, null=True)),
                ('FuturesShortVary', models.IntegerField(blank=True, default='0', max_length=50, null=True)),
            ],
        ),
    ]
