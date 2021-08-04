from django.test import TestCase

from rango.models import AnimalCategory
from django.urls import reverse

"""
Ensures the number of views received for a Category are positive or zero.
"""


class AnimalCategoryMethodTests(TestCase):

    def test_ensure_views_are_positive(self):
        category = AnimalCategory(category_name='test', views=-1)
        category.save()
        self.assertEqual((category.views >= 0), True)


class HomePageTests(TestCase):

    def test_index_view_with_no_categories(self):
        response = self.client.get(reverse('rango:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'There are no categories present.')
        self.assertQuerysetEqual(response.context['categories'], [])


# Create your tests here.
