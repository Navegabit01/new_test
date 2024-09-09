from decimal import Decimal

from ..models import Item

class ItemAdapter:
    def __init__(self, item: Item):
        self.item = item

    def get_identifier(self):
        return self.item.id

    def get_price_without_tax(self):
        return float(self.item.price_without_tax)

    def get_tax(self):
        return float(self.item.tax)

    def calculate_price_with_tax(self):
        return self.get_price_without_tax() * (float(1) + self.get_tax() / float(100))

