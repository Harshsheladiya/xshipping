# Generated by Django 5.0.4 on 2024-04-11 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0013_remove_orderinfo_height_remove_orderinfo_length_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderinfo',
            name='height',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='orderinfo',
            name='length',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='orderinfo',
            name='weight',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='orderinfo',
            name='width',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
