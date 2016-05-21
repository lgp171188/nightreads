# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-21 09:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('subject', models.CharField(max_length=300)),
                ('message', models.TextField()),
                ('targetted_users', models.PositiveIntegerField(null=True)),
                ('is_sent', models.BooleanField(default=False)),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.Post')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
