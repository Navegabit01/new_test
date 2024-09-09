from rest_framework import serializers
from .models import Order, OrderItem
from items.models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    item = ItemSerializer()  # Asegúrate de que este campo se llama `item` en tu modelo OrderItem

    class Meta:
        model = OrderItem
        fields = ['item', 'quantity']  # Asegúrate de que estos campos existan en tu modelo OrderItem

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'created_at', 'items']
