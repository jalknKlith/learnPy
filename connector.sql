import mysql.connector

db = mysql.connector.connect(host='localhost',database='mydb',user='root',password='')
cursor = db.cursor()
cursor.execute('SELECT * FROM customers')
delete_statement = 'DELETE FROM customers WHERE age > 25'
cursor.execute(delete_statement)
db.commit()
print(cursor.rowcount, 'records deleted.')
