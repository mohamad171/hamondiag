# Generated by Django 4.2.7 on 2023-11-09 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poster',
            name='setting',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posters', to='settings.settings'),
        ),
    ]
