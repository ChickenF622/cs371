# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-28 04:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Continent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('continent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Continent')),
            ],
        ),
        migrations.CreateModel(
            name='Prize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.SmallIntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Winner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Organiztion',
            fields=[
                ('winner_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.Winner')),
                ('name', models.CharField(max_length=100)),
            ],
            bases=('main.winner',),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('winner_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.Winner')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=45)),
                ('date_of_birth', models.DateField()),
            ],
            bases=('main.winner',),
        ),
        migrations.AddField(
            model_name='winner',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Country'),
        ),
        migrations.AddField(
            model_name='prize',
            name='winner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Winner'),
        ),
    ]
