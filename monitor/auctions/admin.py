from django.contrib import admin
from web.auctions.models import Category, Item, Bid


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'slug', 'title')


class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'belongs_to', 'added_by', 'title')

class BidAdmin(admin.ModelAdmin):
    list_display = ('id', 'made_against', 'made_by', 'bid_price')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Bid, BidAdmin)