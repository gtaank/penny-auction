from web.auctions.views import item

__author__ = 'verdan'
from django.conf.urls import patterns, url


urlpatterns = patterns('',
                       url(r'^item/(?P<item_code>[^/]+)/success/?$', item.item_detail_success_view,
                           name='item_detail_page_success'),
                       url(r'^item/(?P<item_code>[^/]+)/?$', item.item_detail_view, name='item_detail_page'),

)
