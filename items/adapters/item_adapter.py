from decimal import Decimal

from ..models import Item

class ItemAdapter:
    def __init__(self, item: Item):
        self.item = item

    def get_identifier(self):
        return self.item.id

    def get_price_without_tax(self):
        return self.item.price_without_tax

    def get_tax(self):
        return self.item.tax

    def calculate_price_with_tax(self):
        return self.get_price_without_tax() * (Decimal(1) + self.get_tax() / Decimal(100))

