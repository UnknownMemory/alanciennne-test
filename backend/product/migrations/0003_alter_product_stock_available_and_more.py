# Generated by Django 4.0.4 on 2022-05-12 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_product_product_name_alter_product_tva'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='stock_available',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='stock_ordered',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
