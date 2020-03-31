import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'whisky_fantasy.settings')

import django
django.setup()
from app.models import WhiskyList, UserProfile
from app.tables.Whisky import Whisky
from app.tables.Location import Location
from django.contrib.auth.models import User

def populate():
    whiskies_scotland = [
        {
            'name': 'Aberfeldy Single Malt Scotch Whisky',
            'description': 'Combination of Sweetness, Smoky, Honey, Spicy, Winey, Nutty, Malty, Fruity and Floral',
            'location': 'Aberfeldy',
            'quantity': 4,
            'price': 12.50,
            'merchant': 1,
        },
        {
            'name': 'Balblair Single Malt Scotch Whisky',
            'description': 'Combination of Sweetness, Honey, Winey, Nutty, Malty, Fruity and Floral',
            'location': 'Balblair',
            'quantity': 4,
            'price': 12.50,
            'merchant': 1,
        },
        {
            'name': 'Caol Ila 12 Year Old Single Malt Whisky',
            'description': 'Combination of Sweetness, Malty, Fruity and Floral',
            'location': 'Port Askaig',
            'quantity': 4,
            'price': 12.50,
            'merchant': 1,
        },
        {
            'name': 'Dailuaine 16 Year Old, Flora & Fauna',
            'description': 'Combination of Sweetness, Fruity and Floral',
            'location': 'Strathspey',
            'quantity': 4,
            'price': 12.50,
            'merchant': 1,
        },
        {
            'name': 'Edradour 10 Year Old Highland Single Malt Scotch Whisky',
            'description': 'Combination of Sweetness, Smoky, Medicinal, Honey, Fruity and Floral',
            'location': 'Pitlochry',
            'quantity': 4,
            'price': 12.50,
            'merchant': 1,
        },
        {
            'name': 'Glen Garioch 18 Year Old Scotch Whisky',
            'description': 'Combination of Sweetness, Smoky, Nutty, Malty, Fruity and Floral',
            'location': 'Inverurie',
            'quantity': 4,
            'price': 12.50,
            'merchant': 1,
        },
    ]

    whiskies_ireland = [
        {
            'name': 'Hberfeldy Single Malt Scotch Whisky',
            'description': 'Combination of Sweetness, Smoky, Honey, Spicy, Winey, Nutty, Malty, Fruity and Floral',
            'location': 'Belfast',
            'quantity': 4,
            'price': 12.50,
            'merchant': 1,
        },
        {
            'name': 'Ialblair Single Malt Scotch Whisky',
            'description': 'Combination of Sweetness, Honey, Winey, Nutty, Malty, Fruity and Floral',
            'location': 'Dublin',
            'quantity': 4,
            'price': 12.50,
            'merchant': 1,
        },
        {
            'name': 'Jaol Ila 12 Year Old Single Malt Whisky',
            'description': 'Combination of Sweetness, Malty, Fruity and Floral',
            'location': 'Belfast',
            'quantity': 4,
            'price': 12.50,
            'merchant': 1,
        },
    ]

    no_whiskylist = []

    cats = {
        'Scotland': {'pages': whiskies_scotland, 'views': 128},
        'Northern Ireland': {'pages': whiskies_ireland, 'views': 64},
    }

    merchant = User.objects.create(
        username = "merchant10",
        email = "merchant@test.com",
    )
    merchant.set_password('123456')
    merchant.save()

    merchant_profile = UserProfile.objects.create(
    user = merchant,
    role = 1,
    )


    for cat, cat_data in cats.items():
        c = add_whiskylist(cat, cat_data['views'])
        for p in cat_data['pages']:
            print(merchant.id)
            add_whisky(c, p['name'], p['description'], p['location'], p['quantity'], p['price'],merchant.id)

    # Print out the categories we have added.
    for c in WhiskyList.objects.all():
        for p in Whisky.objects.filter(whisky=c):
            print(f'- {c}: {p}')



# Save Data into Whisky List Model
def add_whiskylist(name, views):
    c = WhiskyList.objects.get_or_create(whisky_category_name=name)[0]
    c.views=views
    c.save()
    return c

# Save Data into Whisky Model
def add_whisky(cat, name, description, location, quantity, price, merchant_id):
    p = Whisky.objects.get_or_create(category=cat, whisky_name=name)[0]
    p.whisky_description=description
    p.whisky_location=Location.objects.get(location_name=location)
    p.whisky_quantity=quantity
    p.whisky_price=price
    p.merchant=User.objects.get(id=merchant_id)
    p.save()
    return p

# Start execution here!
if __name__ == '__main__':
    print('Starting Rango Population Script...')
    populate()
