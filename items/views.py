from rest_framework import viewsets
from rest_framework.response import Response

from .models import Item
from .serializers import ItemSerializer
from .use_cases.item_use_cases import CreateItemUseCase

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def create(self, request, *args, **kwargs):
        use_case = CreateItemUseCase(request.data)
        item_adapter = use_case.execute()
        serializer = self.get_serializer(item_adapter.item)
        data = serializer.data
        data['price_with_tax'] = item_adapter.calculate_price_with_tax()
        return Response(data, status=201)

