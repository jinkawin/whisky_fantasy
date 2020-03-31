import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'whisky_fantasy.settings')

import django
django.setup()
from app.models import Whisky, WhiskyList

def populate():
    whiskies_scotland = [
        {
            'name': 'Aberfeldy Single Malt Scotch Whisky',
            'description': 'Combination of Sweetness, Smoky, Honey, Spicy, Winey, Nutty, Malty, Fruity and Floral',
            'location': 'Aberfeldy',
            'quantity': 4,
            'price': 12.50,
        },
        {
            'name': 'Balblair Single Malt Scotch Whisky',
            'description': 'Combination of Sweetness, Honey, Winey, Nutty, Malty, Fruity and Floral',
            'location': 'Balblair',
            'quantity': 4,
            'price': 12.50,
        },
        {
            'name': 'Caol Ila 12 Year Old Single Malt Whisky',
            'description': 'Combination of Sweetness, Malty, Fruity and Floral',
            'location': 'Port Askaig',
            'quantity': 4,
            'price': 12.50,
        },
        {
            'name': 'Dailuaine 16 Year Old, Flora & Fauna',
            'description': 'Combination of Sweetness, Fruity and Floral',
            'location': 'Strathspey',
            'quantity': 4,
            'price': 12.50,
        },
        {
            'name': 'Edradour 10 Year Old Highland Single Malt Scotch Whisky',
            'description': 'Combination of Sweetness, Smoky, Medicinal, Honey, Fruity and Floral',
            'location': 'Pitlochry',
            'quantity': 4,
            'price': 12.50,
        },
        {
            'name': 'Glen Garioch 18 Year Old Scotch Whisky',
            'description': 'Combination of Sweetness, Smoky, Nutty, Malty, Fruity and Floral',
            'location': 'Inverurie',
            'quantity': 4,
            'price': 12.50,
        },
    ]

    whiskies_ireland = [
        {
            'name': 'Hberfeldy Single Malt Scotch Whisky',
            'description': 'Combination of Sweetness, Smoky, Honey, Spicy, Winey, Nutty, Malty, Fruity and Floral',
            'location': 'Belfast',
            'quantity': 4,
            'price': 12.50,
        },
        {
            'name': 'Ialblair Single Malt Scotch Whisky',
            'description': 'Combination of Sweetness, Honey, Winey, Nutty, Malty, Fruity and Floral',
            'location': 'Dublin',
            'quantity': 4,
            'price': 12.50,
        },
        {
            'name': 'Jaol Ila 12 Year Old Single Malt Whisky',
            'description': 'Combination of Sweetness, Malty, Fruity and Floral',
            'location': 'Belfast',
            'quantity': 4,
            'price': 12.50,
        },
    ]
    no_whisky = []

    cats = {
        'Scotland': {'pages': whiskies_scotland, 'views': 128},
        'Northern Ireland': {'pages': whiskies_ireland, 'views': 64},
    }

    # If you want to add more categories or pages,
    # add them to the dictionaries above.

    # The code below goes through the cats dictionary, then adds each category,
    # and then adds all the associated pages for that category
    for cat, cat_data in cats.items(): # calling add_cat() and add_page() functions repeatedly
        c = add_cat(cat, cat_data['views'])
        for p in cat_data['pages']:
            add_page(c, p['name'], p['description'], p['location'], p['quantity'], p['price'])

    # Print out the categories we have added.
    for c in WhiskyList.objects.all():
        for p in Whisky.objects.filter(whisky=c):
            print(f'- {c}: {p}')

def add_whisky(cat, name, description, location, quantity, price):
    p = Whisky.objects.get_or_create(whiskylist=cat, name=name)[0]
    p.description=url
    p.location=views
    p.quantity=quantity
    p.price=price
    p.save()
    return p

def add_whiskylist(name, views):
    c = WhiskyList.objects.get_or_create(name=name)[0]
    c.views=views
    c.save()
    return c

# Start execution here!
if __name__ == '__main__':
    print('Starting Rango Population Script...')
    populate()
