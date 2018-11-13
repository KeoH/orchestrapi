# Generated by Django 2.1.3 on 2018-11-06 23:53

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_remove_app_last_version'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='app',
            name='cloned',
        ),
        migrations.RemoveField(
            model_name='app',
            name='domain',
        ),
        migrations.RemoveField(
            model_name='app',
            name='git_name',
        ),
        migrations.RemoveField(
            model_name='app',
            name='git_url',
        ),
        migrations.AlterField(
            model_name='app',
            name='data',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default={'cloned': False, 'domain': 'example.com', 'git': {'name': '', 'url': ''}, 'local_build': True, 'max_instances': 1, 'ssl': True}),
        ),
    ]