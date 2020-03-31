import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'whisky_fantasy.settings')

import django

django.setup()

from django.contrib.auth.models import User

from app.models import UserProfile, Whisky
from app.tables.WhiskyList import WhiskyList
from app.tables.Location import Location


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
            'location': 'Balblair',
            'quantity': 4,
            'price': 12.50,

        },
        {
            'name': 'Dailuaine 16 Year Old, Flora & Fauna',
            'description': 'Combination of Sweetness, Fruity and Floral',
            'location': 'Balblair',
            'quantity': 4,
            'price': 12.50,

        },
        {
            'name': 'Edradour 10 Year Old Highland Single Malt Scotch Whisky',
            'description': 'Combination of Sweetness, Smoky, Medicinal, Honey, Fruity and Floral',
            'location': 'Aberfeldy',
            'quantity': 4,
            'price': 12.50,

        },
        {
            'name': 'Glen Garioch 18 Year Old Scotch Whisky',
            'description': 'Combination of Sweetness, Smoky, Nutty, Malty, Fruity and Floral',
            'location': 'Aberfeldy',
            'quantity': 4,
            'price': 12.50,

        },
    ]

    no_whiskylist = []

    cats = {
        'Scotland': {'pages': whiskies_scotland, 'views': 128},
    }
    merchant = User.objects.get_or_create(username="merchant11")[0]
    merchant.set_password('123456')
    merchant.save()

    merchant_profile = UserProfile.objects.get_or_create(user=merchant)[0]
    merchant_profile.role = 1
    merchant_profile.save()

    for cat, cat_data in cats.items():

        for p in cat_data['pages']:

            add_whisky(p['name'], p['description'], p['location'], p['quantity'], p['price'], merchant.id)


# Save Data into Whisky Model
def add_whisky(name, description, location, quantity, price, merchant_id):
    try:
        p = Whisky.objects.create(
            whisky_name=name,
            whisky_description=description,
            whisky_location=Location.objects.get(location_name=location),
            whisky_quantity=20,
            whisky_price=price,
            merchant=User.objects.get(id=merchant_id),
        )
        print(p)
        print("Create successfully")
    except Exception:
        print("please run 'python manage.py loaddata data.json' to load location")


# Start execution here!


if __name__ == '__main__':
    print('Starting Population Script...')
    populate()
