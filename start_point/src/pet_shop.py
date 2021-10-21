# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(shop):
    return shop["name"]

def get_total_cash(shop):
    return shop['admin']['total_cash']

def add_or_remove_cash(shop, i):
    shop['admin']['total_cash'] += i

def get_pets_sold(shop):
    return shop['admin']['pets_sold']

def increase_pets_sold(shop, units):
    shop['admin']['pets_sold'] += units

def get_stock_count(shop):
    return len(shop['pets'])

def get_pets_by_breed(shop, breed):
    breeds = []
    for pet in shop['pets']:
        if pet['breed'] == breed:
            breeds.append(pet)
    return breeds

