from __future__ import absolute_import
from datetime import datetime

from pennyauction.celery import app
from web.auctions.models import Item


@app.task(name='process_bids')
def process_bids():
    auctions_needed_to_process = Item.get_items_needed_to_process()
    print auctions_needed_to_process
    for auction_item in auctions_needed_to_process:
        bids_against_item = auction_item.bids.all().order_by('-bid_price')
        if bids_against_item:
            highest_bid = bids_against_item[0]
            highest_bid.is_a_winner = True
            highest_bid.awarded_on = datetime.now()
            highest_bid.save()

        auction_item.is_active = False
        auction_item.save()
