from pennyauction.libs.renderers import BaseRenderer


class ItemRenderer(BaseRenderer):
    @property
    def latest_bid(self):
        latest_bid = self.bids
        if latest_bid:
            return latest_bid[0]

    @property
    def bids(self):
        return self._item.bids.all().order_by('-bid_price')

    @property
    def min_available_bid(self):
        base_price = self.latest_bid.bid_price if self.latest_bid else self._item.base_price
        return base_price + self._item.price_difference_in_bids

    @property
    def is_active(self):
        return self._item.is_active

    @property
    def winner(self):
        winner_of_auction = self._item.bids.filter(is_a_winner=True)
        return winner_of_auction[0] if winner_of_auction else None

