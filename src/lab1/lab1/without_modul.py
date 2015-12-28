import MySQLdb as Mdb
import sys

def without_rieltor(numline):
    global con
    try:
        con = Mdb.connect('localhost', 'root', '', 'mydb')
        query = "CALL new_procedure();"
        cur = con.cursor(Mdb.cursors.DictCursor)
        cur.execute(query)
        con.commit()
        return cur.fetchall()
    except Mdb.Error, e:
        print "Error %d: %s" % (e.args[0], e.args[1])
        sys.exit(1)
    finally:
        if con:
            con.close()