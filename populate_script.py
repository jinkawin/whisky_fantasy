import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'whisky_fantasy.settings')

import django
django.setup()
from app.models import Whisky

def populate():
    python_pages = [
        {'title': 'Official Python Tutorial',
        'url': 'http://docs.python.org/3/tutorial/',
        'views': 7 },
        {'title': 'How to Think like a Computer Scientist',
        'url': 'http://www.greenteapress.com/thinkpython/',
        'views': 5 },
        {'title': 'Learn Python in 10 Minutes',
        'url': 'http://www.korokithakis.net/tutorials/python/',
        'views': 9}
    ]

    django_pages = [
        {'title': 'Official Django Tutorial',
        'url': 'https://docs.djangoproject.com/en/2.1/intro/tutorial01/',
        'views': 12 },
        {'title': 'Django Rocks',
        'url': 'http://www.djangorocks.com/',
        'views': 14 },
        {'title': 'How to Tango with Django',
        'url': 'http://www.tangowithdjango.com/',
        'views': 16 }
    ]

    other_pages = [
        {'title': 'Bottle',
        'url': 'http://bottlepy.org/docs/dev/',
        'views': 3},
        {'title': 'Flask',
        'url': 'http://flask.pocoo.org',
        'views': 5}
    ]

    no_pages = []

    cats = {
        'Python': {'pages': python_pages, 'views': 128, 'likes': 64},
        'Django': {'pages': django_pages, 'views': 64, 'likes': 32},
        'Other Frameworks': {'pages': other_pages, 'views': 32, 'likes': 16},
        'Pascal': {'pages': no_pages, 'views': 0, 'likes': 0},
        'Perl': {'pages': no_pages, 'views': 0, 'likes': 0},
        'PHP': {'pages': no_pages, 'views': 0, 'likes': 0},
        'Prolog': {'pages': no_pages, 'views': 0, 'likes': 0},
        'PostScript': {'pages': no_pages, 'views': 0, 'likes': 0},
        'Programming': {'pages': no_pages, 'views': 0, 'likes': 0},
    }

    # If you want to add more categories or pages,
    # add them to the dictionaries above.

    # The code below goes through the cats dictionary, then adds each category,
    # and then adds all the associated pages for that category
    for cat, cat_data in cats.items(): # calling add_cat() and add_page() functions repeatedly
        c = add_cat(cat, cat_data['views'], cat_data['likes'])
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'], p['views'])

    # Print out the categories we have added.
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'- {c}: {p}')

def add_whisky(cat, title, url, views=0):
    p = Whisky.objects.get_or_create(category=cat,title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p

# Start execution here!
if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()