# Generated by Django 4.2 on 2023-07-17 02:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('add_asset_invoice', '0051_rename_asset_transfer_assettransferdummy_transfer_asset_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assettransferdummy',
            name='transfer_asset',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='add_asset_invoice.assettransfer', verbose_name='التحويل'),
        ),
    ]
