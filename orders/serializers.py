from rest_framework import serializers
from .models import Order, OrderItem
from items.models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'reference', 'name', 'description', 'price_without_tax', 'tax']

class OrderItemSerializer(serializers.ModelSerializer):
    item = ItemSerializer()  # Serialize the related Item model

    class Meta:
        model = OrderItem
        fields = ['item', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'created_at', 'items']
