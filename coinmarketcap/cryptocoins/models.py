from django.db import models


# Create your models here.
class Cryptocurrency(models.Model):

    slug = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=10)
    rank = models.IntegerField()
    price_usd = models.DecimalField(max_digits=7, decimal_places=2)
    price_btc = models.DecimalField(max_digits=8, decimal_places=7)
    volume_usd_24h = models.DecimalField(max_digits=14, decimal_places=2)
    market_cap_usd = models.DecimalField(max_digits=14, decimal_places=2)
    available_supply = models.DecimalField(max_digits=20, decimal_places=2)
    total_supply = models.DecimalField(max_digits=20, decimal_places=2)
    max_supply = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    percent_change_1h = models.DecimalField(max_digits=5, decimal_places=2)
    percent_change_24h = models.DecimalField(max_digits=5, decimal_places=2)
    percent_change_7d = models.DecimalField(max_digits=5, decimal_places=2)
    last_updated = models.DateTimeField()