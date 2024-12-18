# Generated by Django 5.1.1 on 2024-10-23 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_jobopening_jobapplication'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
