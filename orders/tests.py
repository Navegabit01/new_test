from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from .models import Order, OrderItem
from items.models import Item
from django.contrib.auth import get_user_model

User = get_user_model()

class OrderTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='root', password='Fisyb8o9h*2024')
        self.client.force_authenticate(user=self.user)
        self.item = Item.objects.create(
            reference='REF123',
            name='Test Item',
            description='Test Description',
            price_without_tax='100.00',
            tax='15.00'
        )
        self.order_data = {
            'created_at': '2024-09-01T00:00:00Z'
        }
        self.items_data = [{'item': {'id': self.item.id}, 'quantity': 2}]

    def test_create_order(self):
        response = self.client.post(
            reverse('order-list'),
            {
                'created_at': '2024-09-01T00:00:00Z',
                'items': self.items_data
            }, format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(OrderItem.objects.count(), 1)
        self.assertEqual(OrderItem.objects.first().quantity, 2)

    def test_get_order(self):
        order = Order.objects.create(created_at='2024-09-01T00:00:00Z')
        OrderItem.objects.create(order=order, item=self.item, quantity=2)
        response = self.client.get(reverse('order-detail', kwargs={'pk': order.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
