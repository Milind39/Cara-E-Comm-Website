# Generated by Django 5.0.3 on 2024-04-17 15:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AddField(
            model_name='product',
            name='is_sale',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='sale_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 4, 17, 21, 11, 52, 319486)),
        ),
    ]
