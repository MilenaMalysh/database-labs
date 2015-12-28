__author__ = ""
from bson.code import Code
from models import Customer, House, Rieltor, Company
mapfunc = """
		function(){
			emit(this.rating, 1)
		}
		"""

reducefunc = """
		function reduce(key, values){
		return values.length;
		}
		"""

mapfunc1 = """
		function(){
			emit(this.h_company.con_name, 1)
		}
		"""