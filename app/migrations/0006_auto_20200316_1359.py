# Generated by Django 3.0.4 on 2020-03-16 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_customer_cust_fb_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='cust_fb_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
