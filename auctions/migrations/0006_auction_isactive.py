# Generated by Django 4.1.5 on 2023-04-28 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_category_auction_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='isActive',
            field=models.BooleanField(default=True),
        ),
    ]
