# Generated by Django 4.2.6 on 2023-10-26 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, unique=True)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('picture', models.ImageField(upload_to='pictures')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, null=True, upload_to='pictures')),
            ],
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, null=True)),
                ('color', models.CharField(choices=[('danger', 'red'), ('primary', 'blue'), ('secondary', 'gray'), ('info', 'light blue'), ('dark', 'black'), ('warning', 'yellow')], default='dark', max_length=15)),
                ('font_size', models.CharField(choices=[('h1', 'heading 1'), ('h2', 'heading 2'), ('h3', 'heading 3'), ('h4', 'heading 4'), ('h5', 'heading 5'), ('h6', 'heading 6')], default='h6', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='childs', to='blog.blog')),
            ],
        ),
    ]
