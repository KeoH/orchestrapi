# Generated by Django 2.1.3 on 2019-02-04 23:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_project_networks'),
        ('services', '0004_service_networks'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='services', to='projects.Project'),
        ),
        migrations.AlterField(
            model_name='service',
            name='networks',
            field=models.ManyToManyField(blank=True, related_name='services', to='networks.NetworkBridge'),
        ),
    ]
