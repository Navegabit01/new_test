from ..models import Item
from ..adapters.item_adapter import ItemAdapter

class CreateItemUseCase:
    def __init__(self, item_data):
        self.item_data = item_data

    def execute(self):
        item = Item.objects.create(**self.item_data)
        return ItemAdapter(item)
