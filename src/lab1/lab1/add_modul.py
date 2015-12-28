import MySQLdb as Mdb
import sys
from models import Customer, House, Rieltor, Company

def add_rieltor(company,name,num_wb):
    rieltor = Rieltor(company=company, name=name, num_wb=num_wb)
    rieltor.save()

def add_house(adress,price,sold, passw, num_wb,co_name):
    house = House(adress=adress, price=price, house_sold=sold, h_customer=Customer.objects.get(password=passw), h_rieltor=Rieltor.objects.get(num_wb=num_wb), h_company=Company.objects.get(con_name=co_name))
    house.save()

def add_customer(name, passw, bithday):
    customer = Customer(name=name, password=passw, bith_date=bithday)
    customer.save()

def add_company(name,rating,form):
    company = Company(con_name=name, rating=rating, form=form)
    company.save()