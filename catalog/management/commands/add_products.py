from django.core.management.base import BaseCommand
from catalog.models import Category, Product

class Command(BaseCommand):
    help = 'Add products to database'

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()

        category, _ = Category.objects.get_or_create(name="Игрушки", description="Игрушки детские")

        products = [
            {
                'name': "Машинки",
                'description': "Разные машинки",
                'category': category,
                'purchase_price': "100.00"
            },
            {
                'name': "Конструктор",
                'description': "Конструктор",
                'category': category,
                'purchase_price': "200.00"
            },
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added product: {product.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Product already exist: {product.name}'))