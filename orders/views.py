from rest_framework import viewsets
from rest_framework.response import Response

from .models import Order
from .serializers import OrderSerializer
from .use_cases.order_use_cases import CreateOrderUseCase

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        order_data = request.data['order']
        items_data = request.data['items']
        use_case = CreateOrderUseCase(order_data, items_data)
        order = use_case.execute()
        serializer = self.get_serializer(order.order)
        return Response(serializer.data, status=201)
