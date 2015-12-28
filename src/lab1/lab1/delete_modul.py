import MySQLdb as Mdb
import sys
from models import Customer, House, Rieltor, Company

def delete_rieltor(numline):
    Rieltor.objects.filter(num_wb=numline).delete()

def delete_customer(numline):
    Customer.objects.filter(password=numline).delete()

def delete_house(numline):
    House.objects.filter(adress=numline).delete()

def delete_company(numline):
    Company.objects.filter(con_name=numline).delete()