
#Assicurati di definire il nome del database quando crei la connessione
import mysql.connector
 
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase"
)
 
mycursor = mydb.cursor()
 
mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")  #Per creare una tabella in MySQL, usa l'istruzione
#"CREATE TABLE".
#Crea una tabella denominata "clienti"


###########################################################################################################################################################

#Restituisce un elenco dei database del tuo sistema
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES") #Puoi controllare se esiste una tabella elencando tutte le tabelle nel tuo database con l'istruzione 
#"SHOW TABLES"

for x in mycursor:
  print(x)