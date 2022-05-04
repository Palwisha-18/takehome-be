from django.db import models
from django_extensions.db.models import TimeStampedModel


class Home(TimeStampedModel):
    SingleFamily = "SingleFamily"
    VacantResidentialLand = "VacantResidentialLand"
    Condominium = "Condominium"
    MultiFamily2To4 = "MultiFamily2To4"
    Duplex = "Duplex"
    Apartment = "Apartment"

    HOME_TYPES = [
        (SingleFamily, "SingleFamily"),
        (VacantResidentialLand, "VacantResidentialLand"),
        (Condominium, "Condominium"),
        (MultiFamily2To4, "MultiFamily2To4"),
        (Duplex, "Duplex"),
        (Apartment, "Apartment"),
    ]

    num_bathrooms = models.FloatField(null=True, blank=True)
    num_bedrooms = models.IntegerField(null=True, blank=True)
    home_size = models.IntegerField(null=True, blank=True)
    property_size = models.IntegerField(null=True, blank=True)
    home_type = models.CharField(max_length=50, choices=HOME_TYPES)
    year_built = models.IntegerField(null=True, blank=True)
    tax_value = models.IntegerField()
    tax_year = models.IntegerField()

    address = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    zipcode = models.IntegerField()
    state = models.CharField(max_length=2)

    current_price = models.IntegerField(null=True, blank=True)
    current_rent_price = models.IntegerField(null=True, blank=True)
    last_sold_date = models.DateTimeField(null=True, blank=True)
    last_sold_price = models.IntegerField(null=True, blank=True)

    zillow_id = models.IntegerField()
    zillow_link = models.URLField()
    zillow_rent_estimate_price = models.IntegerField(null=True, blank=True)
    zillow_rent_estimate_price_last_updated = models.DateTimeField(null=True, blank=True)
    zillow_selling_price_estimate = models.IntegerField(null=True, blank=True)
    zillow_selling_price_estimate_last_updated = models.DateTimeField(null=True, blank=True)
