import csv
import logging
import math
import os
import pytz
from api.models import Home
from datetime import datetime
from django.conf import settings
from django.core.management.base import BaseCommand


logger = logging.getLogger('listings_api')
file_path = os.path.abspath(os.path.abspath(settings.BASE_DIR) + '/sample-data/data.csv')
price_units = {'K': 1000, 'M': 1000000}


class Command(BaseCommand):
    help = 'Imports data about houses'

    @staticmethod
    def price_converter(price, unit):
        return price * price_units[unit]

    @staticmethod
    def date_converter(date):
        date = date.split("/")
        if len(date) == 1:
            return None
        return datetime(month=int(date[0]), day=int(date[1]), year=int(date[2]), tzinfo=pytz.UTC)

    def populate_home_model(self):
        try:
            with open(file_path, mode="r") as csv_file:

                csv_reader = csv.DictReader(csv_file)
                objects_list = []
                for row in csv_reader:
                    try:
                        objects_list.append(Home(
                            num_bathrooms=row["bathrooms"] or None,
                            num_bedrooms=row["bedrooms"] or None,
                            home_size=row["home_size"] or None,
                            property_size=row["property_size"] or None,
                            home_type=row["home_type"],
                            year_built=row["year_built"] or None,
                            tax_value=int(float(row["tax_value"])),
                            tax_year=row["tax_year"],

                            address=row["address"],
                            city=row["city"],
                            zipcode=row["zipcode"],
                            state=row["state"],

                            current_price=self.price_converter(float(row["price"][1:-1]), row["price"][-1]),
                            current_rent_price=row["rent_price"] or None,
                            last_sold_date=self.date_converter(row["last_sold_date"]),
                            last_sold_price=row["last_sold_price"] or None,

                            zillow_id=row["zillow_id"],
                            zillow_link=row["link"],
                            zillow_rent_estimate_price=row["rentzestimate_amount"] or None,
                            zillow_rent_estimate_price_last_updated=self.date_converter(row["rentzestimate_last_updated"]),
                            zillow_selling_price_estimate=row["zestimate_amount"] or None,
                            zillow_selling_price_estimate_last_updated=self.date_converter(row["zestimate_last_updated"]),
                        ))
                    except Exception as e:
                        logger.info(f"Exception: {e}")
                try:
                    Home.objects.bulk_create(objects_list)
                except Exception as e:
                    logger.info(f"Exception: {e}")

        except Exception as e:
            logger.info(f"Exception: {e}")

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        homes_queryset = Home.objects.all()
        if homes_queryset.exists():
            self.stdout.write("House Data Already Populated")
        else:
            self.stdout.write("Starting to populate house data")
            self.populate_home_model()
            num_houses = len(Home.objects.all())
            self.stdout.write("Import Completed: {} populated".format(num_houses))
