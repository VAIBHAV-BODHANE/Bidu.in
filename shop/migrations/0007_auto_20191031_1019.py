# Generated by Django 2.2.6 on 2019-10-31 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_orders_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='phone',
            field=models.CharField(max_length=20),
        ),
    ]
