import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django

django.setup()
from rango.models import AnimalCategory


# For an explanation of what is going on here, please refer to the TwD book.

def populate():
    python_pages = [
        {'title': 'Official Python Tutorial',
         'url': 'http://docs.python.org/3/tutorial/',
         'views': 114, },
        {'title': 'How to Think like a Computer Scientist',
         'url': 'http://www.greenteapress.com/thinkpython/',
         'views': 53},
        {'title': 'Learn Python in 10 Minutes',
         'url': 'http://www.korokithakis.net/tutorials/python/',
         'views': 20}]

    django_pages = [
        {'title': 'Official Django Tutorial',
         'url': 'https://docs.djangoproject.com/en/2.1/intro/tutorial01/',
         'views': 32},
        {'title': 'Django Rocks',
         'url': 'http://www.djangorocks.com/',
         'views': 12},
        {'title': 'How to Tango with Django',
         'url': 'http://www.tangowithdjango.com/',
         'views': 1258}]

    other_pages = [
        {'title': 'Bottle',
         'url': 'http://bottlepy.org/docs/dev/',
         'views': 54},
        {'title': 'Flask',
         'url': 'http://flask.pocoo.org',
         'views': 64}]

    no_pages = []

    cats = {'Python': {'pages': python_pages, 'views': 128, 'likes': 64},
            'Django': {'pages': django_pages, 'views': 64, 'likes': 32},
            'Other Frameworks': {'pages': other_pages, 'views': 32, 'likes': 16},
            'Pascal': {'pages': no_pages, 'views': 0, 'likes': 0},
            'Perl': {'pages': no_pages, 'views': 0, 'likes': 0},
            'PHP': {'pages': no_pages, 'views': 0, 'likes': 0},
            'Prolog': {'pages': no_pages, 'views': 0, 'likes': 0},
            'PostScript': {'pages': no_pages, 'views': 0, 'likes': 0},
            'Programming': {'pages': no_pages, 'views': 0, 'likes': 0}, }

    for cat, cat_data in cats.items():
        c = add_cat(cat, views=cat_data['views'], likes=cat_data['likes'])


def add_cat(name, views=0, likes=0):
    c = AnimalCategory.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c


# Start execution here!
if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()
