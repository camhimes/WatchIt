from django.core.management.base import BaseCommand
from watches.scraper.scraper import scrape_watches

class Command(BaseCommand):
    help = 'Scrapes watch data from Amazon'

    def handle(self, *args, **kwargs):
        scrape_watches()
        self.stdout.write(self.style.SUCCESS('Successfully scraped watch prices.'))
