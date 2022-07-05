# Generated by Django 2.2.28 on 2022-07-05 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Repo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('sha', models.UUIDField()),
            ],
        ),
        migrations.CreateModel(
            name='Commit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sha', models.UUIDField()),
                ('author', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('date', models.DateTimeField()),
                ('message', models.TextField()),
                ('url', models.SlugField()),
                ('comment_count', models.IntegerField()),
                ('repo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='playground.Repo')),
            ],
        ),
    ]
