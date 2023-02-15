import mysql.connector
 
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Animali"
)
 
mycursor = mydb.cursor()

sql = "INSERT INTO Mammiferi ( PersonID, Nome_proprio , Razza v, Peso , Eta ) VALUES (%s, %s)"
val = [
  ("Elefante"),
  ("Giraffa"),
  ("Lombrico"),
  ("Zebra"),
  ("Leone")
]
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")