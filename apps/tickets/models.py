from decimal import Decimal
from django.db import models


class Ticket(models.Model):

    name = models.CharField(max_length=100)
    price = models.FloatField()

    @property
    def early_bird_price(self):
        price = self.price * 0.8
        return price