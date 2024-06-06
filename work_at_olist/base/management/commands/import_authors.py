import argparse
import csv

from django.core.management.base import BaseCommand
from work_at_olist.base.models import Author

BATCH_SIZE = 1000


class Command(BaseCommand):
    help = 'Imports authors from a .csv file and saves to database.'

    def add_arguments(self, parser):
        parser.add_argument('csv', type=argparse.FileType(mode='r', encoding='utf-8'))

    def handle(self, *args, **options):
        count, total, batch = 0, 0, []
        with open(options['csv'].name, mode='r', encoding='utf-8', newline='') as authors:
            csv_reader = csv.reader(authors)
            for line in csv_reader:
                if line[0] == 'name':
                    continue
                batch.append(Author(name=line[0]))
                count += 1
                total += 1
                if count == BATCH_SIZE:
                    Author.objects.bulk_create(batch)
                    count = 0
                    batch.clear()
            if batch:
                Author.objects.bulk_create(batch)
            self.stdout.write(f'{total} authors created.')
