# Generated by Django 5.0.3 on 2024-08-18 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_alter_product_image_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='images/'),
        ),
    ]
