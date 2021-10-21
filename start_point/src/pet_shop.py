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

def find_pet_by_name(shop, name):
    for pet in shop['pets']:
        if pet['name'] == name:
            return pet

def remove_pet_by_name(shop, name):
    for pet in shop['pets']:
        if name == pet['name']:
            shop['pets'].remove(pet)

def add_pet_to_stock(shop, new_pet):
    shop['pets'].append(new_pet)
        
def get_stock_count(shop):
    return len(shop['pets'])

def get_customer_cash(customer):
    return customer['cash']

def remove_customer_cash(customer, i):
    customer['cash'] -= i

def get_customer_pet_count(customer):
    return len(customer['pets'])

def add_pet_to_customer(customer, new_pet):
    customer['pets'].append(new_pet)

def customer_can_afford_pet(customer, new_pet):
    return customer['cash'] >= new_pet['price']