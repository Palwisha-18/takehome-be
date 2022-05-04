import json
from api.models import Home
from django.urls import reverse
from rest_framework.test import APITestCase


class TestHome(APITestCase):

    def setUp(self):
        home = Home.objects.create(**{
                "num_bathrooms": 2.0,
                "num_bedrooms": 4,
                "home_size": 2263,
                "property_size": 43043,
                "home_type": "SingleFamily",
                "year_built": 1960,
                "tax_value": 2034729,
                "tax_year": 2017,
                "address": "24629 Wingfield Rd",
                "city": "Hidden Hills",
                "zipcode": 91302,
                "state": "CA",
                "current_price": 2580000,
                "current_rent_price": None,
                "last_sold_date": "2018-03-28T00:00:00Z",
                "last_sold_price": 2575000,
                "zillow_id": 19882763,
                "zillow_link": "https://www.zillow.com/homedetails/24629-Wingfield-Rd-Hidden-Hills-CA-91302/19882763_zpid/",
                "zillow_rent_estimate_price": 10000,
                "zillow_rent_estimate_price_last_updated": "2018-08-07T00:00:00Z",
                "zillow_selling_price_estimate": 2617942,
                "zillow_selling_price_estimate_last_updated": "2018-08-07T00:00:00Z"
            }
        )
        self.home_uuid = home.uuid
        self.home_list_url = reverse("home-list")
        self.home_retrieve_update_delete_url = reverse("retrieve-update-delete-home", args=(self.home_uuid,))

    def test_home_list(self):
        # python manage.py test api.tests.TestHome.test_home_list

        response = self.client.get(self.home_list_url)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertEqual(1, len(response_data))

    def test_home_retrieve(self):
        # python manage.py test api.tests.TestHome.test_home_retrieve

        response = self.client.get(self.home_retrieve_update_delete_url)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertEqual(str(self.home_uuid), response_data['uuid'])
