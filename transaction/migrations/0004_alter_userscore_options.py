# Generated by Django 4.2 on 2024-11-02 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0003_alter_transaction_transaction_type_userscore_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userscore',
            options={'permissions': [('has_permission_score', 'user has score permission')]},
        ),
    ]
