# Generated by Django 5.0.4 on 2024-04-11 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0017_alter_orderinfo_height_alter_orderinfo_length_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderinfo',
            name='height',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='length',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='width',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
    ]
