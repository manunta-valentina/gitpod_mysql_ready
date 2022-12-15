 #mostra l'elenco dei database del mio sistema

import mysql.connector 
mydb = mysql.connector.connect(
 host="localhost",
  user="root",
  password=""
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")  #Puoi controllare se esiste un database elencando tutti i database nel tuo sistema usando l'istruzione 
#"SHOW DATABASES":

for x in mycursor:
  print(x)

  #######################################################################################################################
#puoi provare ad accedere al database quando effettui la connessione

  import mysql.connector
 
mydb = mysql.connector.connect(  #Per connetterci al database
  host="localhost",
  user="root",
  password="",
  database="mydatabase"
)
#Se il database non esiste, riceverai un errore.


