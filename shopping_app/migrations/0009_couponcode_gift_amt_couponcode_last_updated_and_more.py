# Generated by Django 4.1.5 on 2023-01-25 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_app', '0008_giftcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='couponcode',
            name='gift_amt',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='couponcode',
            name='last_updated',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.DeleteModel(
            name='GiftCode',
        ),
    ]
