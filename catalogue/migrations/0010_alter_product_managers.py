# Generated by Django 4.2 on 2024-11-01 22:15

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0009_product_is_active'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='product',
            managers=[
                ('default_manager', django.db.models.manager.Manager()),
            ],
        ),
    ]
