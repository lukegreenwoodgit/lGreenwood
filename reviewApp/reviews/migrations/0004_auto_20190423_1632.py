# Generated by Django 2.2 on 2019-04-23 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20190423_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='avg_cost',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
    ]
