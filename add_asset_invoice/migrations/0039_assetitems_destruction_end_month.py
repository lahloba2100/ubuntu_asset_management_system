# Generated by Django 4.2 on 2023-06-28 11:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('add_asset_invoice', '0038_assetitems_destruction_start_month'),
    ]

    operations = [
        migrations.AddField(
            model_name='assetitems',
            name='destruction_end_month',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='نهاية الاهلاك'),
        ),
    ]
