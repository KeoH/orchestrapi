# Generated by Django 2.1.3 on 2018-11-13 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_image_app'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='app',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='apps.App'),
        ),
    ]
