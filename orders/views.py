from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemSerializer
from items.models import Item

class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows orders to be viewed or edited.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        """
        Create a new order along with its items.
        """
        order_data = request.data
        items_data = order_data.pop('items', [])

        # Validate and create the Order
        serializer = self.get_serializer(data=order_data)
        serializer.is_valid(raise_exception=True)
        order = serializer.save()

        # Create associated OrderItems
        self._create_order_items(order, items_data)

        # Serialize and return response
        response_serializer = self.get_serializer(order)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)

    def _create_order_items(self, order, items_data):
        """
        Create order items based on the provided item data.
        """
        for item_data in items_data:
            item_id = item_data['item']['id']
            item = Item.objects.get(id=item_id)
            OrderItem.objects.create(order=order, item=item, quantity=item_data['quantity'])
