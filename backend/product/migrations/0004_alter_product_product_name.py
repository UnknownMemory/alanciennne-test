# Generated by Django 4.0.4 on 2022-05-13 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_product_stock_available_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
