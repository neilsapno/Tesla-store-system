# Generated by Django 4.2.10 on 2024-12-15 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_orders_order_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='order_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='order_time',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
