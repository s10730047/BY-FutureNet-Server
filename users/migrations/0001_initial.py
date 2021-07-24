# Generated by Django 3.2.4 on 2021-06-07 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=70)),
                ('password', models.CharField(default='', max_length=200)),
                ('token', models.CharField(default='', max_length=300)),
            ],
        ),
    ]
