# Generated by Django 2.1.5 on 2020-03-19 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20200316_2253'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('addressOne', models.TextField(max_length=100)),
                ('addressTwo', models.TextField(blank=True, max_length=100)),
                ('town_city', models.CharField(max_length=40)),
                ('postcode', models.CharField(max_length=6)),
                ('phone', models.PositiveIntegerField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Merchant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('merchant_username', models.CharField(max_length=255)),
                ('merchant_password', models.CharField(max_length=255)),
                ('merchant_email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trans_status', models.CharField(default=1, max_length=1)),
                ('trans_time', models.DateTimeField(editable=False)),
                ('trans_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('trans_quantity', models.PositiveIntegerField()),
                ('trans_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Customer')),
                ('merchant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Merchant')),
                ('trans_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Delivery')),
            ],
        ),
        migrations.CreateModel(
            name='Whisky',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(blank=True, max_length=255)),
                ('whisky_name', models.CharField(max_length=255)),
                ('whisky_description', models.CharField(max_length=255)),
                ('whisky_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('whisky_quantity', models.PositiveIntegerField()),
                ('whisky_status', models.CharField(default=1, max_length=255)),
                ('whisky_img_link', models.CharField(blank=True, max_length=255)),
                ('whisky_img', models.ImageField(blank=True, upload_to='product_images')),
            ],
        ),
        migrations.AddField(
            model_name='transaction',
            name='whisky',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Whisky'),
        ),
    ]
