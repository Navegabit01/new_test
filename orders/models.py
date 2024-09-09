from django.db import models
from items.models import Item


class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    def get_total_without_tax(self):
        return sum(item.price_without_tax * item.orderitem_set.get(item=item).quantity for item in self.items.all())

    def get_total_with_tax(self):
        return sum(item.price_without_tax * (1 + item.tax / 100) * item.orderitem_set.get(item=item).quantity for item in self.items.all())

    def __str__(self):
        return str(self.id)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.item.name} ({self.quantity})"
