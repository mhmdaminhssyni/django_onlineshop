# Generated by Django 4.2 on 2024-10-27 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0005_alter_product_brand_alter_product_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
    ]
