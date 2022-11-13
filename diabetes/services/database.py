import mysql.connector

mydb = mysql.connector.connect(
  host="db4free.net",
  user="troncosofranco",
  password="databasetest2022",
  port = 3306, #for Mamp users
  database='register_databas'
)