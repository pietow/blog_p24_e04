# Generated by Django 4.2.18 on 2025-01-28 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, default='my_slug', max_length=200),
        ),
    ]
