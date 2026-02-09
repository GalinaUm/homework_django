from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

from catalog.models import Product

class Command(BaseCommand):
    help = 'Создает группы, назначает разрешения'

    def handle(self, *args, **options):
        moderator_group, created = Group.objects.get_or_create(
            name='Модератор'
        )

        product_ct = ContentType.objects.get_for_model(Product)

        permissions = Permission.objects.filter(
            content_type=product_ct,
            codename__in=[
                'delete_product',
                'can_unpublish_product',
            ]
        )

        moderator_group.permissions.set(permissions)

        self.stdout.write(
            self.style.SUCCESS('Группа "Модератор" создана и настроена')
        )
