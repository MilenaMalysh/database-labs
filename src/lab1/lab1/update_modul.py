import MySQLdb as Mdb
import sys
from models import Customer, House, Rieltor, Company

def update_rieltor(company,name,num_wb):
    Rieltor.objects.filter(num_wb=num_wb).update(company=company, name=name)

def update_house(adress,price,house_sold, customer_pass, rieltor_num_wb,construction_company_con_name,old_adr):
    House.objects.filter(adress=old_adr).update( price=price, house_sold=house_sold, h_customer = customer_pass, h_rieltor=rieltor_num_wb, h_company=construction_company_con_name)

def update_customer(name, passw, bithday,old_pass):
    Customer.objects.filter(password=old_pass).update(name=name,  bith_date=bithday)

def update_company(name,rating,form,old_name):
    Company.objects.filter(con_name=old_name).update( rating=rating, form=form)
