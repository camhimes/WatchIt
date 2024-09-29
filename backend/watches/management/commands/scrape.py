from django.core.management.base import BaseCommand
from watches.scraper.scraper import scrape_watch_prices

class Command(BaseCommand):
    help = 'Scrapes watch price data from Amazon'

    def handle(self, *args, **kwargs):
        scrape_watch_prices()
        self.stdout.write(self.style.SUCCESS('Successfully scraped watch prices.'))
