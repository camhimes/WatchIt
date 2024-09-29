from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .scraper.scraper import scrape_watch_prices

@shared_task
def scrape_watch_prices_task():
    scrape_watch_prices()
