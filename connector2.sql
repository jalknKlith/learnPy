import mysql.connector

cnx = mysql.connector.connect(user='username', password='password', host='localhost', database='testdb')
cursor = cnx.cursor()
cursor.execute('SELECT * FROM employees')
for (employee) in cursor:
  print(employee)
cnx.close()
