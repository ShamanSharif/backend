# Generated by Django 5.1.1 on 2024-09-30 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_googlereview_star_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='googlereview',
            name='display_on_website',
        ),
        migrations.RemoveField(
            model_name='googlereview',
            name='star_rating',
        ),
        migrations.AddField(
            model_name='googlereview',
            name='rating',
            field=models.DecimalField(decimal_places=1, default=5.0, max_digits=2),
        ),
        migrations.AlterField(
            model_name='googlereview',
            name='reviewer_image',
            field=models.ImageField(upload_to='reviewers/'),
        ),
        migrations.AlterField(
            model_name='googlereview',
            name='reviewer_name',
            field=models.CharField(max_length=100),
        ),
    ]
