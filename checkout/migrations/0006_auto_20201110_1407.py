# Generated by Django 3.1.1 on 2020-11-10 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_order_booking_required'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='booking_required',
            new_name='schedule_required',
        ),
    ]