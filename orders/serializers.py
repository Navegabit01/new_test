from rest_framework import serializers
from .models import Order, OrderItem
from items.models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    item = ItemSerializer()  # Serializa el `Item` relacionado

    class Meta:
        model = OrderItem
        fields = ['item', 'quantity']  # Incluye los campos correctos

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'created_at', 'items']
