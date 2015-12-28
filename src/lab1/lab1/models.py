# Create your models here.
from django.db import models
from django_mongodb_engine.contrib import MongoDBManager
from djangotoolbox.fields import ListField, EmbeddedModelField


class Customer(models.Model):

	name = models.CharField(max_length=20)
	password = models.CharField(max_length=45, primary_key=True, db_column='pass')
	bith_date = models.DateField()


class Rieltor(models.Model):

	company = models.IntegerField()
	name = models.CharField(max_length=45)
	num_wb = models.IntegerField(primary_key=True)


class Company(models.Model):

    con_name = models.CharField(max_length=20, primary_key=True)
    rating = models.IntegerField()
    form = models.CharField(max_length=15)
    objects=MongoDBManager()


class House(models.Model):

    h_rieltor = EmbeddedModelField('Rieltor')
    h_company = EmbeddedModelField('Company')
    h_customer = EmbeddedModelField('Customer')
    adress = models.CharField(max_length=40,primary_key=True)
    price = models.IntegerField()
    house_sold = models.BooleanField()
    objects=MongoDBManager()