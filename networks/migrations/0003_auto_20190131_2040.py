# Generated by Django 2.1.3 on 2019-01-31 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('networks', '0002_networkbridge_network_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='networkbridge',
            name='network_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
