# Generated by Django 3.2.6 on 2021-09-06 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstpage', '0003_alter_product_listing_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='productLink',
            field=models.URLField(blank=True, null=True),
        ),
    ]
