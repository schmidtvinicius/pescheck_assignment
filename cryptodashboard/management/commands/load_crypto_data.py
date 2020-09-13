import json
from datetime import datetime

from django.core.management import BaseCommand

from cryptodashboard.models import CryptoCurrency, Article
from pytz import UTC


DATETIME_FORMAT = '%m/%d/%Y %H:%M'

CRYPTOS_AVAILABLE = 'cryptos_available.json'

ALREDY_LOADED_ERROR_MESSAGE = """
If you need to reload the pet data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""

def load_crypto_currencies():
    raw_data = open(CRYPTOS_AVAILABLE, 'r')
    crypto_json = json.loads(raw_data.read())
    if not CryptoCurrency.objects.exists():
        for crypto in crypto_json:
            currency = CryptoCurrency()
            currency.name = crypto["name"]
            currency.code = crypto["code"]
            currency.save()

    # Show this when the user types help
    # help = "Loads data from pet_data.csv into our Pet mode"

    # def handle(self, *args, **options):
    #     if Vaccine.objects.exists() or Pet.objects.exists():
    #         print('Pet data already loaded...exiting.')
    #         print(ALREDY_LOADED_ERROR_MESSAGE)
    #         return
    #     print("Creating vaccine data")
    #     for vaccine_name in VACCINES_NAMES:
    #         vac = Vaccine(name=vaccine_name)
    #         vac.save()
    #     print("Loading pet data for pets available for adoption")
    #     for row in DictReader(open('./pet_data.csv')):
    #         pet = Pet()
    #         pet.name = row['Pet']
    #         pet.submitter = row['Submitter']
    #         pet.species = row['Species']
    #         pet.breed = row['Breed']
    #         pet.description = row['Pet Description']
    #         pet.sex = row['Sex']
    #         pet.age = row['Age']
    #         raw_submission_date = row['submission date']
    #         submission_date = UTC.localize(
    #             datetime.strptime(raw_submission_date, DATETIME_FORMAT))
    #         pet.submission_date = submission_date
    #         pet.save()
    #         raw_vaccination_names = row['vaccinations']
    #         vaccination_names = [name for name in raw_vaccination_names.split('| ') if name]
    #         for vac_name in vaccination_names:
    #             vac = Vaccine.objects.get(name=vac_name)
    #             pet.vaccinations.add(vac)
    #         pet.save()
