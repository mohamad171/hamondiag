# Generated by Django 4.2.6 on 2023-10-30 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postinfo',
            name='post_method',
            field=models.CharField(choices=[('noramal', 'عادی'), ('fast', 'پیشتاز')], default='noramal', max_length=15),
        ),
    ]
