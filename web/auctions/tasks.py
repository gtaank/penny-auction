from __future__ import absolute_import

from celery.task import task
from django.utils import timezone
from pennyauction.celery import app
from web.auctions.models import Item


@app.task(name='process_bids')
def process_bids():
    print "alpha"
    return

    auctions_needed_to_process = Item.get_items_needed_to_process()
    for auction_item in auctions_needed_to_process:
        bids_against_item = auction_item.bids.all().order_by('-bid_price')
        if bids_against_item:
            highest_bid = bids_against_item[0]
            highest_bid.is_a_winner = True
            highest_bid.awarded_on = timezone.now()
            highest_bid.save()
        else:
            continue

        auction_item.is_active = False
        auction_item.save()
