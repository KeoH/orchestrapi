# Generated by Django 2.1.3 on 2019-02-04 23:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_auto_20190205_0017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='project',
        ),
    ]