# Generated by Django 2.1.3 on 2019-03-04 22:25

import core.mixins
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Server',
            fields=[
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('location', models.GenericIPAddressField(verbose_name='Server IP Location')),
                ('port', models.CharField(default='12001', max_length=5, verbose_name='Daemon port')),
            ],
            options={
                'abstract': False,
            },
            bases=(core.mixins.SerializeMixin, models.Model),
        ),
    ]