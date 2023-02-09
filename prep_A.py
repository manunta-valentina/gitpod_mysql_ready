import mysql.connector
 
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Animali"
)
 
mycursor = mydb.cursor()
 
mycursor.execute("CREATE TABLE Mammiferi (ID (int), Nome_proprio VARCHAR(255), Razza (varchar), Peso (int), Eta (int))
