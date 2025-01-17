# Generated by Django 5.1.3 on 2024-12-19 04:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0005_remove_booking_price_per_ticket_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='price_per_ticket',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='event_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bookings.event'),
        ),
    ]
