import os

from django.contrib.auth import get_user_model
from django.core.management import call_command
from django.core.management.base import NoArgsCommand

from web.auctions.models import Item, Category


User = get_user_model()


class Command(NoArgsCommand):
    help = 'Insert Test Data'

    def _header(self, message, is_title=False):
        self.stdout.write('%s %s %s' % ((is_title and '#' or '>') * 20, message, (is_title and '#' or '<') * 20))

    def handle_noargs(self, **options):
        dev_null = open(os.devnull, 'w')
        self.stdout.write('~~ Inserting Test Data for Penny Auction ~~')
        self.stdout.write('Updating Migrations.')
        call_command('migrate', interactive=False, stdout=dev_null, verbosity=0)
        self.stdout.write('Re-creating database TABLES..')
        call_command('flush', interactive=False, stdout=dev_null)
        call_command('migrate', fake=True, stdout=dev_null, verbosity=0)


        user = User.objects.create_superuser(email='verdan.mahmood@gmail.com', password='123456')
        user_1 = User.objects.create_user(email='testuser+1@gmail.com', password='123456')
        user_1.first_name = 'User1'
        user_1.save()

        user_2 = User.objects.create_user(email='testuser+2@gmail.com', password='123456')
        user_2.first_name = 'User2'
        user_2.save()

        user_3 = User.objects.create_user(email='testuser+3@gmail.com', password='123456')
        user_3.first_name = 'User3'
        user_3.save()

        user_4 = User.objects.create_user(email='testuser+4@gmail.com', password='123456')
        user_4.first_name = 'User4'
        user_4.save()

        electronics = Category(slug='electronics', title='Electronics')
        electronics.save()

        cell_phones = Category(slug='cell-phones', title='Cell Phones')
        cell_phones.save()

        laptops = Category(slug='laptops', title='Laptops')
        laptops.save()

        items = []

        items.append(Item(belongs_to=electronics, added_by=user_1, title='My Electronic 1'))
        items.append(Item(belongs_to=electronics, added_by=user_2, title='My Electronic 2'))
        items.append(Item(belongs_to=electronics, added_by=user_2, title='My Electronic 3'))
        items.append(Item(belongs_to=cell_phones, added_by=user_2, title='My Cell Phone 1'))
        items.append(Item(belongs_to=cell_phones, added_by=user_3, title='My Cell Phone 2'))

        items.append(Item(belongs_to=laptops, added_by=user_4, title='My Laptop 1'))

        Item.objects.bulk_create(items)

