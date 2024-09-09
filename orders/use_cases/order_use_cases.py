from ..models import Order, OrderItem
from ..adapters.order_adapter import OrderAdapter
from items.models import Item


class CreateOrderUseCase:
    def __init__(self, items_data):
        self.items_data = items_data

    def execute(self):
        order = Order.objects.create()
        for item_data in self.items_data:
            item = Item.objects.get(id=item_data['item_id'])
            OrderItem.objects.create(order=order, item=item, quantity=item_data['quantity'])
        return OrderAdapter(order)
