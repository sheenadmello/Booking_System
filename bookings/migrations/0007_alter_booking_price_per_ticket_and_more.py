# Generated by Django 5.1.3 on 2024-12-19 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0006_booking_price_per_ticket_alter_booking_event_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='price_per_ticket',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='price_per_ticket',
            field=models.PositiveIntegerField(),
        ),
    ]