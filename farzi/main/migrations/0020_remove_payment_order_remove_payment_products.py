# Generated by Django 4.2.2 on 2023-10-11 04:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_payment_products_orderitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='order',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='products',
        ),
    ]
