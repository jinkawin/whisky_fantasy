# Generated by Django 2.1.5 on 2020-03-15 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20200315_0926'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='is_customer',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='role',
            field=models.CharField(choices=[('Customer', 'customer'), ('Merchant', 'merchant')], default='', max_length=10),
            preserve_default=False,
        ),
    ]
