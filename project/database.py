import mysql.connector
# users="uxgtn0bfj2zq9dph"
# host="bmjlxcdp5kyobevzlkym-mysql.services.clever-cloud.com"
# password="KWns6piTS2HUDWXydzLl"	
# database = "bmjlxcdp5kyobevzlkym"
users="root"
host="localhost"
database="dm"
password=""
def select(q):
	cnx = mysql.connector.connect(user=users, password=password, host=host, database=database)
	cur = cnx.cursor(dictionary=True)
	cur.execute(q)
	result = cur.fetchall()
	cur.close()
	cnx.close()
	return result
def update(q):
	cnx = mysql.connector.connect(user=users, password=password, host=host, database=database)
	cur = cnx.cursor(dictionary=True)
	cur.execute(q)
	cnx.commit()
	result = cur.rowcount
	cur.close()
	cnx.close()
	return result
def delete(q):
	cnx = mysql.connector.connect(user=users, password=password, host=host, database=database)
	cur = cnx.cursor(dictionary=True)
	cur.execute(q)
	cnx.commit()
	result = cur.rowcount
	cur.close()
	cnx.close()
	return result
def insert(q):
	cnx = mysql.connector.connect(user=users, password=password, host=host, database=database)
	cur = cnx.cursor(dictionary=True)
	cur.execute(q)
	cnx.commit()
	result = cur.lastrowid
	cur.close()
	cnx.close()
	return result