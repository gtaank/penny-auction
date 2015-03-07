from django.utils import timezone
from django.utils.text import slugify

__author__ = 'verdan'
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Category(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=255, default='')

    @staticmethod
    def _slugify_by_default(kwargs):
        slug = kwargs.get('slug')
        if slug:
            slug = slugify(unicode(slug))
            kwargs['slug'] = slug

    def __init__(self, *args, **kwargs):
        self._slugify_by_default(kwargs)
        super(Category, self).__init__(*args, **kwargs)


class AuctionItem(models.Model):

    belongs_to = models.ForeignKey('auctions.Category', related_name='auctions')
    added_by = models.ForeignKey('users.User', related_name='auctions')

    title = models.CharField(max_length=255, default='')
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='item/images')
    is_active = models.BooleanField(default=True)

    condition = models.CharField(choices=(('new', 'Brand New'), ('used', 'Slightly Used'), ('old', 'Very Old')))
    number_of_pieces = models.PositiveIntegerField(default=1)

    base_price = models.FloatField(default=0.01)
    shipping_charges = models.FloatField(default=0.00)
    price_difference_in_bids = models.FloatField(default=0.01)

    auction_start_period = models.DateTimeField(default=timezone.now)
    auction_end_period = models.DateTimeField(blank=True, null=True)


class Bid(models.Model):
    made_by = models.ForeignKey('users.User', related_name='bids')
    made_against = models.ForeignKey('auctions.AuctionItem', related_name='bids')
    made_on = models.DateTimeField(auto_now_add=True)

    bid_price = models.FloatField()

    is_a_winner = models.BooleanField(default=False)
    awarded_on = models.DateTimeField()