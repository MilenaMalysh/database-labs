from django.conf.urls import patterns, include, url
from django.contrib import admin
from src.lab1.lab1 import views

urlpatterns = patterns('views',
    # Examples:
    # url(r'^$', 'lab1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^hello/', views.hello, name='hello'),
    url(r'^data/', views.current_datetime, name='current_datetime'),
    #url(r'^', views.menu, name='menu'),
    url(r'^time/plus/(\d{1,2})/$', views.hours_ahead),
    url(r'^house/update$', views.updated_house, name='updated_house'),

    url(r'^house/search$', views.house, name='searched_house'),
    url(r'^house/delete$', views.deleted_house, name='deleted_house'),
    url(r'^house/add$', views.added_house, name='added_house'),
    url(r'^house/change$', views.changed_house, name='changed_house'),
    url(r'^house', views.house, name='house'),
    url(r'^customer/add$', views.added_customer, name='added_customer'),

    url(r'^customer/delete$', views.deleted_customer, name='deleted_customer'),
    url(r'^customer/change$', views.changed_customer, name='changed_customer'),
    url(r'^customer/search$', views.customer, name='searched_customer'),
    url(r'^customer/update$', views.updated_customer, name='updated_customer'),
    url(r'^customer', views.customer, name='customer'),

    url(r'^rieltor/add$', views.added_rieltor, name='added_rieltor'),
    url(r'^rieltor/update$', views.updated_rieltor, name='updated_rieltor'),
    url(r'^rieltor/delete$', views.deleted_rieltor, name='deleted_rieltor'),
    url(r'^rieltor/change$', views.changed_rieltor, name='changed_rieltor'),
    url(r'^rieltor/search$', views.rieltor, name='searched_rieltor'),
    url(r'^rieltor', views.rieltor, name='rieltor'),

    url(r'^construction_company/sort$', views.sorted_company, name='sorted_company'),
    url(r'^construction_company/add$', views.added_company, name='added_company'),
    url(r'^construction_company/delete$', views.deleted_company, name='deleted_company'),
    url(r'^construction_company/change$', views.changed_company, name='changed_company'),
    url(r'^construction_company/update$', views.updated_company, name='updated_company'),
    url(r'^construction_company', views.construction_company, name='construction_company'),

    url(r'^$', views.menu),

)
