# Generated by Django 5.0.4 on 2024-04-07 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0007_orderinfo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OrderInfo',
        ),
    ]
