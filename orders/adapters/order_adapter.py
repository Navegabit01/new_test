from ..models import Order

class OrderAdapter:
    def __init__(self, order: Order):
        self.order = order

    def get_identifier(self):
        return self.order.id

    def get_total_without_tax(self):
        return self.order.get_total_without_tax()

    def get_total_with_tax(self):
        return self.order.get_total_with_tax()
