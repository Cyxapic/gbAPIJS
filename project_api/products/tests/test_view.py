from django.test import TestCase, Client

from rest_framework import status

from products.models import Category, Product
from products.serializers import ProductSerializer



IMAGE = 'https://via.placeholder.com/150'

MOCK_DATA = {
    'categories': ('Первая', 'Вторая'),
    'products': (
        {
            'category': None,
            'title': 'Первый товар',
            'price': 1000,
            'img': IMAGE,
        },
        {
            'category': None,
            'title': 'Второй товар',
            'price': 1200,
            'img': IMAGE,
        },
    )
}


class TestViews(TestCase):
    """ Test module for GET all products"""
    client = Client()
    def setUp(self):
        category = Category.objects.create(title=MOCK_DATA['categories'][0])
        for data in MOCK_DATA['products']:
            data['category'] = category
            Product.objects.create(**data)

    def test_get_all_prod(self):
        resp = self.client.get('/api/v1/products/')
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        self.assertEqual(resp.data, serializer.data)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
