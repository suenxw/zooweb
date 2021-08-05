from django.test import TestCase
from registration.forms import User

from rango.models import AnimalCategory
from django.urls import reverse


def add_category(name, views):
    category = AnimalCategory.objects.get_or_create(category_name=name)[0]
    category.views = views
    category.save()
    return category


class SlugTest(TestCase):
    def test_artist_slugify_works(self):
        category = AnimalCategory(category_name='This is a test')
        category.save()
        self.assertEqual(category.slug, 'this-is-a-test')


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


class AddCategoryTest(TestCase):
    def test_index_view_with_categories(self):
        add_category('Tiger', 1)
        add_category('Bird', 5)
        add_category('Elephant', 10)
        add_category('Lion', 10)
        add_category('Whale', 100)
        response = self.client.get(reverse('rango:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Tiger')
        self.assertContains(response, 'Bird')
        self.assertContains(response, 'Elephant')
        self.assertContains(response, 'Lion')
        self.assertContains(response, 'Whale')
        numberofcategories = len(response.context['categories'])
        self.assertEquals(numberofcategories, 5)
# Create your tests here.
