# Generated by Django 3.0.4 on 2020-03-16 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200316_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='cust_fb_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]