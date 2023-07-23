from functions import add, view, update_service_date
from classes import Car
import random
from files import load_items

def create_cars(num:int=0):
    for i in range(num):
        owner=f"owner{i}"
        name=random.choice(['mazda', 'toyota', 'bmw', 'audi', 'hyundai', 'tesla', 'mercecdes'])
        license=random.randrange(60000000, 80000000)
        year=random.randrange(2010, 2023)
        visit_date=f"{random.randrange(1,31)}-{random.randrange(1,12)}-{random.randrange(2020,2023)}"
        service_date=f"{random.randrange(1,31)}-{random.randrange(1,12)}-{random.randrange(2020,2023)}"
        history_service = service_date
        add(Car(name=name, year=year, color=random.choice(['red', 'blue', 'gold', 'silver', 'green']), license=license, owner=owner, visit_date=visit_date, service_date=service_date, service_history=history_service))
    view()



create_cars(40)

def get_license(num):
    cars = load_items()
    return cars[num].license

l = get_license(5)

update_service_date(license=l, date="10.10.10")
view()
