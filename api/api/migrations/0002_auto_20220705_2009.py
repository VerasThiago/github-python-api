# Generated by Django 2.2.28 on 2022-07-05 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commit',
            name='sha',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='commit',
            name='url',
            field=models.URLField(max_length=128),
        ),
        migrations.AlterField(
            model_name='repo',
            name='sha',
            field=models.CharField(max_length=128),
        ),
    ]