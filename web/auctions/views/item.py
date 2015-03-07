from django.core.urlresolvers import reverse
from django.shortcuts import redirect

from pennyauction.libs.views import BaseView
from web.auctions.forms.bid import BidForm
from web.auctions.models import Item, Bid
from web.auctions.renderers import ItemRenderer


class ItemDetailView(BaseView):
    template_name = 'auctions/item_detail.html'

    def get(self, item_code, success):
        item = Item.get_item(item_code=item_code)
        if item:
            item = ItemRenderer(item)
            bid_form = BidForm(initial={'bid': item.min_available_bid})
            return self.get_context_data(item=ItemRenderer(item), form=bid_form, success=success)
        else:
            return self.get_context_data()

    def post(self, item_code, success):
        item = Item.get_item(item_code=item_code)
        item_renderer = ItemRenderer(item)
        bid_form = BidForm(self.request.POST, initial={'bid': item_renderer.min_available_bid})
        if not bid_form.is_valid():
            return self.get_context_data(item=item, form=bid_form)

        Bid.add_new_bid(made_by=self.request.user, made_against=item, bid_price=bid_form.cleaned_data.get('bid'))
        return redirect(reverse('item_detail_page_success', kwargs={'item_code': item.id}))


def item_detail_view(request, item_code, success=None):
    return ItemDetailView(request).respond_with(item_code=item_code, success=success)

def item_detail_success_view(request, item_code):
    return ItemDetailView(request).respond_with(item_code=item_code, success=True)