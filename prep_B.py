import mysql.connector
 
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Animali"
)
mycursor = mydb.cursor()


sql = "INSERT INTO Mammiferi2 ( Nome_proprio , Razza , Peso , Eta ) VALUES ( %s, %s, %s, %s)"
val = [
  ( "Dumbo", "Elefante", 500, 69),
  ( "Nano" , "Giraffa", 100, 3),
  ( "Enrico", "Lombrico", 1, 100),
  ( "Marti", "Zebra", 70, 5),
  ( "Alex", "Leone", 101, 6)
]
mycursor.executemany(sql, val)


mydb.commit()


print(mycursor.rowcount, "was inserted.")

#Verifica tramite la console dei comandi di aver inserito gli animali nel DB


mysql  #nei comandi 
show databases ;
use Animali ;
 select * from Mammiferi ;