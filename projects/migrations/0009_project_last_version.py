# Generated by Django 2.1.2 on 2018-10-31 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_auto_20181030_2234'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='last_version',
            field=models.CharField(default='latest', max_length=30),
        ),
    ]