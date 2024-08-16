from csv import DictReader
from datetime import datetime

from django.core.management import BaseCommand

from anime.models import Anime
from pytz import UTC


DATETIME_FORMAT = '%m/%d/%Y %H:%M'


ALREDY_LOADED_ERROR_MESSAGE = """
If you need to reload the Anime data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from pet_data.csv into our Pet mode"

    def handle(self, *args, **options):
        if Anime.objects.exists():
            print('Anime data already loaded...exiting.')
            print(ALREDY_LOADED_ERROR_MESSAGE)
            return
        print("Loading Anime data")
        for row in DictReader(open('./anime_data.csv')):
            anime = Anime()
            anime.name = row['Anime']
            anime.producer = row['Producer']
            anime.description = row['Description']
            raw_release_date = row['Release Date']
            release_date = UTC.localize(
                datetime.strptime(raw_release_date, DATETIME_FORMAT))
            anime.release_date = release_date
            anime.save()