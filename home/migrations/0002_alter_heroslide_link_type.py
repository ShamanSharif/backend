# Generated by Django 5.1.1 on 2024-09-22 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='heroslide',
            name='link_type',
            field=models.CharField(choices=[('phone', 'Phone Number'), ('url', 'URL'), ('id', 'Page Section ID')], default='url', max_length=10),
        ),
    ]
