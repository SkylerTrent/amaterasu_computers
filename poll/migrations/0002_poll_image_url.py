# Generated by Django 3.1.1 on 2020-11-09 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='image_url',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
    ]
