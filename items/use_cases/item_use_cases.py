from ..models import Item
from ..adapters.item_adapter import ItemAdapter

class CreateItemUseCase:
    def __init__(self, item_data):
        self.item_data = item_data

    def execute(self):
        # Validaciones básicas
        self.item_data['price_without_tax'] = float(self.item_data['price_without_tax'])
        if self.item_data['price_without_tax'] < 0:
            raise ValueError("El precio no puede ser negativo.")
        if not (0 <= self.item_data['tax'] <= 100):
            raise ValueError("El impuesto debe estar entre 0 y 100.")

        item = Item.objects.create(**self.item_data)
        return ItemAdapter(item)

