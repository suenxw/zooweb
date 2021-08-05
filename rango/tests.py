from django.test import TestCase
from registration.forms import User

from rango.models import AnimalCategory
from django.urls import reverse

"""
Ensures the number of views received for a Category are positive or zero.
"""


def create_user_object():
    """
    Helper function to create a User object.
    """
    user = User.objects.get_or_create(username='testuser',
                                      email='test@test.com')[0]
    user.set_password('testabc123')
    user.save()

    return user


def create_super_user_object():
    return User.objects.create_superuser('admin', 'admin@test.com', 'testpassword')


def test_model_admin_interface_inclusion(self):
    """
        Attempts to access the UserProfile admin interface instance.
        If we don't get a HTTP 200, then we assume that the model has not been registered. Fair assumption!
        """
    super_user = create_super_user_object()
    self.client.login(username='admin', password='testpassword')

    # The following URL should be available if the UserProfile model has been registered to the admin interface.
    response = self.client.get('/admin/rango/profile/')
    self.assertEqual(response.status_code, 200, )


def add_category(name, views=0, likes=0):
    category = AnimalCategory.objects.get_or_create(name=name)[0]
    category.views = views
    category.likes = likes

    category.save()
    return category


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
