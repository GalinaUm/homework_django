from itertools import product

from django.conf import settings
from django.core.cache import cache

from catalog.models import Product
from config.settings import CACHE_ENABLE

from .models import Product


class ProductService:

    @staticmethod
    def get_products_from_caches():
        """Получает данные по продуктам из кэша, если кэш пуст, получает данные из бд"""
        if not CACHE_ENABLE:
            return Product.objects.all()
        key = "products_list"
        products = cache.get(key)
        if products is not None:
            return products
        products = Product.objects.all()
        cache.set(key, products)
        return products

    @staticmethod
    def get_products_by_category(category_pk):
        """Возвращает кэшированный список продуктов для конкретной категории"""
        if not settings.CACHE_ENABLE:
            return Product.objects.filter(category_id=category_pk, status=Product.PUBLISHED)
        key = f'products_category_{category_pk}'
        products = cache.get(key)
        if products is None:
            products = Product.objects.filter(status=Product.PUBLISHED)
            cache.set(key, products, 60 * 15)
        return products

    @staticmethod
    def get_all_products():
        key = 'all_products'
        products = cache.get(key)
        if products is None:
            products = Product.objects.filter(status=Product.PUBLISHED)
            cache.set(key, products, 60 * 15)
        return products

