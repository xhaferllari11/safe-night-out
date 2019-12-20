# Generated by Django 2.2.6 on 2019-12-20 18:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('drink_type', models.CharField(choices=[('B', 'beer'), ('W', 'wine'), ('L', 'liquor'), ('C', 'cocktail'), ('S', 'spiked')], max_length=100)),
                ('abv', models.IntegerField()),
                ('cost', models.IntegerField()),
                ('time_consumed', models.DateTimeField()),
                ('effects', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='DrinkSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('duration', models.IntegerField()),
                ('drinks', models.ManyToManyField(to='main_app.Drink')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=250)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.DrinkSession')),
            ],
        ),
    ]