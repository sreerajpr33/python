import mysql.connector


con = mysql.connector.connect(
    host="localhost",
    user="sreeraj",
    password="sree12345687", 
    database="mydatabase"   
)
cursor = con.cursor()


cursor.execute("CREATE TABLE IF NOT EXISTS emp (emp_id INT, address text,experiance int,position text)")





