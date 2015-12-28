__author__ = 'Milena'
from django.http.response import Http404,HttpResponse
import datetime
import delete_modul, update_modul,without_modul
import add_modul,sort_modul
from xml.dom.minidom import parse, parseString
from django.template.loader import get_template
from django.template import Context, RequestContext
from django.shortcuts import render_to_response
from models import Customer, House, Rieltor, Company

from pymongo import Connection

from src.lab1.lab1 import get_tables

def hello(request):
    return HttpResponse("Hello world!")

def current_datetime(request):
    now = datetime.datetime.now()
    return render_to_response('current_datetime.html', {'current_date': now})

def menu(request):
    return render_to_response('menu.html', {'Name': "Houses Databases",'Header1':'house','Header2':'rieltor','Header3':'customer','Header4': 'construction_company'})

def house(request):
    houses = get_tables.get_houses()
    template= get_template("houses.html")
    context = RequestContext(request,{"request": request, 'houses_list': houses,'Name': "house",'Header1':'rieltor','Header2':'customer','Header3': 'construction_company'})
    return HttpResponse(template.render(context))

def rieltor(request):
    rieltors = get_tables.get_rieltors()
    template= get_template("rieltors.html")
    context = RequestContext(request,{"request": request, 'rieltors_list': rieltors,'Name': "rieltor",'Header1':'house','Header2':'customer','Header3': 'construction_company'})
    return HttpResponse(template.render(context))

def customer(request):
    customers = get_tables.get_customers()
    template= get_template("customers.html")
    context = RequestContext(request,{"request": request, 'customers_list': customers,'Name': "customer",'Header1':'house','Header2':'rieltor','Header3': 'construction_company'})
    return HttpResponse(template.render(context))





def construction_company(request):
    construction_companies = get_tables.get_construction_companies()
    template= get_template("construction_companies.html")
    context = RequestContext(request,{"request": request, 'construction_companies_list': construction_companies,'Name': "construction_company",'Header1':'house','Header2':'rieltor','Header3':'customer'})
    return HttpResponse(template.render(context))

def deleted_rieltor(request):
    id = request.GET.get("id", 0)
    delete_modul.delete_rieltor(id)
    rieltors = get_tables.get_rieltors()
    template= get_template("rieltors.html")
    context = RequestContext(request,{"request": request, 'rieltors_list': rieltors,'Name': "rieltor",'Header1':'house','Header2':'customer','Header3': 'construction_company'})
    return HttpResponse(template.render(context))




def deleted_house(request):
    id = request.GET.get("id", 0)
    delete_modul.delete_house(id)
    houses = get_tables.get_houses()
    template= get_template("houses.html")
    context = RequestContext(request,{"request": request, 'houses_list': houses,'Name': "house",'Header1':'rieltor','Header2':'customer','Header3': 'construction_company'})
    return HttpResponse(template.render(context))


def deleted_customer(request):
    id = request.GET.get("id", 0)
    delete_modul.delete_customer(id)
    customers = get_tables.get_customers()
    template= get_template("customers.html")
    context = RequestContext(request,{"request": request, 'customers_list': customers,'Name': "customer",'Header1':'house','Header2':'rieltor','Header3': 'construction_company'})
    return HttpResponse(template.render(context))


def deleted_company(request):
    id = request.GET.get("id", 0)
    delete_modul.delete_company(id)
    construction_companies = get_tables.get_construction_companies()
    template= get_template("construction_companies.html")
    context = RequestContext(request,{"request": request, 'construction_companies_list': construction_companies,'Name': "construction_company",'Header1':'house','Header2':'rieltor','Header3':'customer'})
    return HttpResponse(template.render(context))





def added_rieltor(request):
    new_com_rieltor= request.POST.get("new_com_rieltor",0)
    new_name_rieltor= request.POST.get("new_name_rieltor",0)
    new_num_wb_rieltor= request.POST.get("new_num_wb_rieltor",0)
    if new_num_wb_rieltor == '':
        xml = parse('D:\\WorkTable\\Projects\\ODBlab1\\src\\lab1\\lab1\\rieltors.xml')
        num_wb = xml.getElementsByTagName('num_wb')
        for node in num_wb:
            new_num_wb_rieltor=node.childNodes[0].nodeValue
        name = xml.getElementsByTagName('name')
        for node in name:
            new_name_rieltor=node.childNodes[0].nodeValue
        company = xml.getElementsByTagName('company')
        for node in company:
            new_com_rieltor=node.childNodes[0].nodeValue
    add_modul.add_rieltor(new_com_rieltor,new_name_rieltor,new_num_wb_rieltor)
    rieltors = get_tables.get_rieltors()
    template= get_template("rieltors.html")
    context = RequestContext(request,{"request": request, 'rieltors_list': rieltors,'Name': "rieltor",'Header1':'house','Header2':'customer','Header3': 'construction_company'})
    return HttpResponse(template.render(context))


def added_house(request):
    new_house_adress= request.POST.get("new_house_adress",0)
    new_house_price= request.POST.get("new_house_price",0)
    new_house_sold= request.POST.get("new_house_sold",0)
    new_house_customer_pass= request.POST.get("new_house_customer_pass",0)
    new_house_rielor_num_wb= request.POST.get("new_house_rielor_num_wb",0)
    new_house_company_co_name= request.POST.get("new_house_company_co_name",0)
    if new_house_adress == '':
        xml = parse('D:\\WorkTable\\Projects\\ODBlab1\\src\\lab1\\lab1\\houses.xml')
        adr = xml.getElementsByTagName('adr')
        for node in adr:
            new_house_adress=node.childNodes[0].nodeValue
        price = xml.getElementsByTagName('price')
        for node in price:
            new_house_price=node.childNodes[0].nodeValue
        sold = xml.getElementsByTagName('sold')
        for node in sold:
            new_house_sold=node.childNodes[0].nodeValue
        passp = xml.getElementsByTagName('pass')
        for node in passp:
            new_house_customer_pass=node.childNodes[0].nodeValue
        num_wb = xml.getElementsByTagName('num_wb')
        for node in num_wb:
            new_house_rielor_num_wb=node.childNodes[0].nodeValue
        con_name = xml.getElementsByTagName('con_name')
        for node in con_name:
            new_house_company_co_name=node.childNodes[0].nodeValue
    add_modul.add_house(new_house_adress,new_house_price,new_house_sold,new_house_customer_pass,new_house_rielor_num_wb,new_house_company_co_name)
    houses = get_tables.get_houses()
    template= get_template("houses.html")
    context = RequestContext(request,{"request": request, 'houses_list': houses,'Name': "house",'Header1':'rieltor','Header2':'customer','Header3': 'construction_company'})
    return HttpResponse(template.render(context))


def added_customer(request):
    new_customer_name= request.POST.get("new_customer_name",0)
    new_customer_pass= request.POST.get("new_customer_pass",0)
    new_customer_bith_date= request.POST.get("new_customer_bith_date",0)
    if new_customer_pass == '':
        xml = parse('D:\\WorkTable\\Projects\\ODBlab1\\src\\lab1\\lab1\\customers.xml')
        name = xml.getElementsByTagName('name')
        for node in name:
            new_customer_name=node.childNodes[0].nodeValue
        passp = xml.getElementsByTagName('pass')
        for node in passp:
            new_customer_pass=node.childNodes[0].nodeValue
        bith = xml.getElementsByTagName('bithday')
        for node in bith:
            new_customer_bith_date=node.childNodes[0].nodeValue
    add_modul.add_customer(new_customer_name,new_customer_pass,new_customer_bith_date)
    customers = get_tables.get_customers()
    template= get_template("customers.html")
    context = RequestContext(request,{"request": request, 'customers_list': customers,'Name': "customer",'Header1':'house','Header2':'rieltor','Header3': 'construction_company'})
    return HttpResponse(template.render(context))


def added_company(request):
    new_company_con_name= request.POST.get("new_company_con_name",0)
    new_company_rating= request.POST.get("new_company_rating",0)
    new_company_form= request.POST.get("new_company_form",0)
    if new_company_con_name == '':
        xml = parse('D:\\WorkTable\\Projects\\ODBlab1\\src\\lab1\\lab1\\company.xml')
        name = xml.getElementsByTagName('name')
        for node in name:
            new_company_con_name=node.childNodes[0].nodeValue
        rating = xml.getElementsByTagName('rating')
        for node in rating:
            new_company_rating=node.childNodes[0].nodeValue
        form = xml.getElementsByTagName('form')
        for node in form:
            new_company_form=node.childNodes[0].nodeValue
    add_modul.add_company(new_company_con_name,new_company_rating,new_company_form)
    construction_companies = get_tables.get_construction_companies()
    template= get_template("construction_companies.html")
    context = RequestContext(request,{"request": request, 'construction_companies_list': construction_companies,'Name': "construction_company",'Header1':'house','Header2':'rieltor','Header3':'customer'})
    return HttpResponse(template.render(context))


def changed_rieltor(request):
    num_wb = request.GET.get("num_wb", 0)
    company = request.GET.get("company", 0)
    name = request.GET.get("name", 0)
    template= get_template("rieltors_ch.html")
    context = RequestContext(request,{"request": request, "id": id, 'num_wb': num_wb, 'company': company,'name': name})
    return HttpResponse(template.render(context))


def changed_house(request):
    adr = request.GET.get("adr", 0)
    price = request.GET.get("price", 0)
    sold = request.GET.get("sold", 0)
    passw = request.GET.get("passw", 0)
    num_wb = request.GET.get("num_wb", 0)
    con_name = request.GET.get("con_name", 0)
    template= get_template("houses_ch.html")
    context = RequestContext(request,{"request": request,'adress':adr,'price':price, 'house_sold':sold,'rieltor_num_wb':num_wb,'construction_company_con_name':con_name,'customer_pass':passw})
    return HttpResponse(template.render(context))


def changed_customer(request):
    passw = request.GET.get("passw", 0)
    name = request.GET.get("name", 0)
    bith_date = request.GET.get("bithday", 0)
    template= get_template("customers_ch.html")
    context = RequestContext(request,{"request": request, 'passw':passw, 'name':name,'bith_date':bith_date})
    return HttpResponse(template.render(context))


def changed_company(request):
    name = request.GET.get("name", 0)
    rat = request.GET.get("rat", 0)
    form = request.GET.get("form", 0)
    template= get_template("construction_companies_ch.html")
    context = RequestContext(request,{"request": request, 'name':name, 'rat':rat,'form':form})
    return HttpResponse(template.render(context))


def updated_rieltor(request):
    ch_com_rieltor= request.POST.get("ch_com_rieltor",0)
    ch_name_rieltor= request.POST.get("ch_name_rieltor",0)
    ch_num_wb_rieltor= request.POST.get("ch_num_wb_rieltor",0)
    update_modul.update_rieltor(ch_com_rieltor,ch_name_rieltor,ch_num_wb_rieltor)
    rieltors = get_tables.get_rieltors()
    template= get_template("rieltors.html")
    context = RequestContext(request,{"request": request, 'rieltors_list': rieltors,'Name': "rieltor",'Header1':'house','Header2':'customer','Header3': 'construction_company'})
    return HttpResponse(template.render(context))

def updated_house(request):
    ch_adr_house= request.POST.get("ch_adr_house",0)
    ch_pr_house= request.POST.get("ch_pr_house",0)
    ch_so_house= request.POST.get("ch_so_house",0)
    ch_num_wb_rieltor= request.POST.get("ch_num_wb_rieltor",0)
    ch_name_company= request.POST.get("ch_name_company",0)
    ch_pas_customer= request.POST.get("ch_pas_customer",0)
    old_adr= request.POST.get("old_adr",0)
    update_modul.update_house(ch_adr_house,ch_pr_house,ch_so_house,ch_pas_customer, ch_num_wb_rieltor,ch_name_company,old_adr)
    houses = get_tables.get_houses()
    template= get_template("houses.html")
    context = RequestContext(request,{"request": request, 'houses_list': houses,'Name': "house",'Header1':'rieltor','Header2':'customer','Header3': 'construction_company'})
    return HttpResponse(template.render(context))


def updated_customer(request):
    ch_name_cus= request.POST.get("ch_name_cus",0)
    ch_pass_cus= request.POST.get("ch_pass_cus",0)
    ch_bith_cus= request.POST.get("ch_bith_cus",0)
    old_pass_cus= request.POST.get("old_pass_cus",0)
    update_modul.update_customer(ch_name_cus,ch_pass_cus,ch_bith_cus,old_pass_cus)
    customers = get_tables.get_customers()
    template= get_template("customers.html")
    context = RequestContext(request,{"request": request, 'customers_list': customers,'Name': "customer",'Header1':'house','Header2':'rieltor','Header3': 'construction_company'})
    return HttpResponse(template.render(context))


def updated_company(request):
    ch_name_com= request.POST.get("ch_name_com",0)
    ch_rat_com= request.POST.get("ch_rat_com",0)
    ch_form_com= request.POST.get("ch_form_com",0)
    old_name_com= request.POST.get("old_name_com",0)
    update_modul.update_company(ch_name_com,ch_rat_com,ch_form_com,old_name_com)
    construction_companies = get_tables.get_construction_companies()
    template= get_template("construction_companies.html")
    context = RequestContext(request,{"request": request, 'construction_companies_list': construction_companies,'Name': "construction_company",'Header1':'house','Header2':'rieltor','Header3':'customer'})
    return HttpResponse(template.render(context))

def sorted_company(request):
    companies_s = Company.objects.map_reduce(sort_modul.mapfunc, sort_modul.reducefunc, out='temp',delete_collection=True)
    template= get_template("construction_companies.html")
    context = RequestContext(request,{"request": request, 'construction_companies_list': result,'Name': "construction_company",'Header1':'house','Header2':'rieltor','Header3':'customer'})
    return HttpResponse(template.render(context))

def sorted_house(request):
    houses_s = House.objects.map_reduce(sort_modul.mapfunc1, sort_modul.reducefunc, out='temp',delete_collection=True)
    template= get_template("houses.html")
    context = RequestContext(request,{"request": request, 'houses_list': houses,'Name': "house",'Header1':'rieltor','Header2':'customer','Header3': 'construction_company'})
    return HttpResponse(template.render(context))

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)