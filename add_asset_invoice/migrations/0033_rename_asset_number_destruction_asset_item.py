# Generated by Django 4.2 on 2023-06-24 07:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('add_asset_invoice', '0032_alter_assetitems_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='destruction',
            old_name='asset_number',
            new_name='asset_item',
        ),
    ]
