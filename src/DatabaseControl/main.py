__author__ = 'Esquilo'
import MySQLdb as mdb
import sys

clients_table = 'client_table'
product_table = 'product_table'
sales_table = 'sales_table'
shops_table = "shop_table"

try:
    con = mdb.connect('localhost', 'root', '', 'mydb')
    cur = con.cursor()
    with con:
        cur.execute("SHOW TABLES")
        #query = "INSERT INTO " + clients_table + " VALUES ('Ivan', 'Prymak', 'Konstantinovich', 20, 0)"
        #query = "CREATE TABLE IF NOT EXISTS shop_table (id INT NOT NULL,name VARCHAR(45) NULL,adress VARCHAR(45) NULL,PRIMARY KEY (id))"
        #query = "INSERT INTO " + shops_table +" VALUES (1, 'Shop1', 'Address1')"
        query = "SELECT * FROM " + clients_table
        cur.execute(query)
        rows = cur.fetchall()
        for row in rows:
            print row
except mdb.Error, e:
    print "Error %d: %s" % (e.args[0], e.args[1])
    sys.exit(1)
finally:
    if con:
        con.close()