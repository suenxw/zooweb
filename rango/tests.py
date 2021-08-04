from django.test import TestCase

from rango.models import AnimalCategory

"""
Ensures the number of views received for a Category are positive or zero.
"""


class AnimalCategoryMethodTests(TestCase):

    def test_ensure_views_are_positive(self):
        category = AnimalCategory(category_name='test', views=-1)
        category.save()
        self.assertEqual((category.views >= 0), True)
# Create your tests here.
