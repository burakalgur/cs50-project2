# Generated by Django 4.1.5 on 2023-04-25 08:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_auction_alter_user_email_comment_bid'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='creator',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='auction_creator', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]