
import sys
from string import strip


import sys
from string import strip

from models import Customer, Rieltor,Company, House


def get_houses():
    houses = House.objects.all()
    return houses

def get_rieltors():
    rieltors = Rieltor.objects.all()
    return rieltors

def get_customers():
    customers = Customer.objects.all()
    return customers

def get_construction_companies():
    companies = Company.objects.all()
    return companies




