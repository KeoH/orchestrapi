# Generated by Django 2.1.3 on 2019-03-04 22:25

from django.db import migrations, models
import files.models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0005_auto_20190210_0130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configfile',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=files.models.update_config_file),
        ),
    ]