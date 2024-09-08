from rest_framework import viewsets
from .models import Item
from .serializers import ItemSerializer
from .use_cases.item_use_cases import CreateItemUseCase

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def create(self, request, *args, **kwargs):
        use_case = CreateItemUseCase(request.data)
        item = use_case.execute()
        serializer = self.get_serializer(item.item)
        return Response(serializer.data, status=201)
