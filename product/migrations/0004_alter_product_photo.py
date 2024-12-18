# Generated by Django 5.0.4 on 2024-11-05 13:15

import django_resized.forms
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_product_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], force_format='WEBP', keep_meta=True, quality=100, scale=None, size=[350, 250], upload_to='product/%Y/%m', verbose_name='photo'),
        ),
    ]
