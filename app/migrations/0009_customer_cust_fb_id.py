# Generated by Django 3.0.4 on 2020-03-16 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_remove_customer_cust_fb_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='cust_fb_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
