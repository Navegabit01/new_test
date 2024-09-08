from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Item

class ItemTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.item_data = {
            'reference': 'REF123',
            'name': 'Test Item',
            'description': 'Test Description',
            'price_without_tax': '100.00',
            'tax': '15.00'
        }

    def test_create_item(self):
        response = self.client.post('/api/items/', self.item_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Item.objects.count(), 1)

    def test_get_item(self):
        item = Item.objects.create(**self.item_data)
        response = self.client.get(f'/api/items/{item.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Item')
