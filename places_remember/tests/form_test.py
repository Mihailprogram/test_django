from django.test import TestCase
from places.forms import PlaceForm


class PlaceFormTestCase(TestCase):
    def test_form_with_valid_data(self):
        form_data = {
            'name': 'Test Place',
            'comment': 'Test Comment',
            'latitude': 55.76,
            'longitude': 37.64
        }
        form = PlaceForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_with_missing_data(self):
        form_data = {
            'name': 'Test Place',
            'latitude': 55.76,
            'longitude': 37.64
        }
        form = PlaceForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_form_with_invalid_data(self):
        form_data = {
            'name': '',
            'comment': 'Test Comment',
            'latitude': 55.76,
            'longitude': 37.64
        }
        form = PlaceForm(data=form_data)
        self.assertFalse(form.is_valid())
