# Generated by Django 4.2.7 on 2023-11-13 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0002_alter_poster_setting'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='phone',
            field=models.PositiveBigIntegerField(),
        ),
    ]