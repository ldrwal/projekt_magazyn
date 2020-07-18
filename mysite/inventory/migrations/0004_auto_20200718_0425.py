# Generated by Django 3.0.8 on 2020-07-18 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20200718_0348'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Part',
            new_name='Item',
        ),
        migrations.AlterField(
            model_name='stockitem',
            name='quantity',
            field=models.DecimalField(decimal_places=0, default=1, max_digits=15, verbose_name='Stock Quantity'),
        ),
    ]