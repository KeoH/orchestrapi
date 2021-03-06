# Generated by Django 2.1.2 on 2018-11-06 22:33

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('git_url', models.URLField(blank=True, null=True)),
                ('git_name', models.CharField(blank=True, max_length=50, null=True)),
                ('domain', models.CharField(blank=True, max_length=255, null=True)),
                ('data', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict)),
                ('last_version', models.CharField(default='latest', max_length=30)),
                ('params', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict)),
                ('cloned', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
