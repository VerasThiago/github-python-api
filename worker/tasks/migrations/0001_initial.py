# Generated by Django 4.0.6 on 2022-07-13 03:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Repo',
            fields=[
                ('id',
                 models.BigAutoField(auto_created=True,
                                     primary_key=True,
                                     serialize=False,
                                     verbose_name='ID')),
                ('owner', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Commit',
            fields=[
                ('id',
                 models.BigAutoField(auto_created=True,
                                     primary_key=True,
                                     serialize=False,
                                     verbose_name='ID')),
                ('sha', models.CharField(max_length=128)),
                ('author', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('date', models.DateTimeField()),
                ('message', models.TextField()),
                ('url', models.URLField(max_length=128)),
                ('comment_count', models.IntegerField()),
                ('repo',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   to='tasks.repo')),
            ],
        ),
    ]
