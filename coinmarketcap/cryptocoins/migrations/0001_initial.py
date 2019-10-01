# Generated by Django 2.0.4 on 2019-09-26 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cryptocurrency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('symbol', models.CharField(max_length=30)),
                ('rank', models.CharField(max_length=30)),
                ('price_usd', models.CharField(max_length=30)),
                ('price_btc', models.CharField(max_length=30)),
                ('volume_usd_24h', models.CharField(max_length=30)),
                ('market_cap_usd', models.CharField(max_length=30)),
                ('available_supply', models.CharField(max_length=30)),
                ('total_supply', models.CharField(max_length=30)),
                ('max_supply', models.CharField(max_length=30)),
                ('percent_change_1h', models.CharField(max_length=30)),
                ('percent_change_24h', models.CharField(max_length=30)),
                ('percent_change_7d', models.CharField(max_length=30)),
                ('last_updated', models.CharField(max_length=30)),
            ],
        ),
    ]
