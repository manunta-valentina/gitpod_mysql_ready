
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

###########################################################################################################################################################
 
  import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
#Quando crei una tabella, dovresti anche creare una colonna con una chiave univoca per ogni record.
#Questo può essere fatto definendo una PRIMARY KEY.
#Usiamo l'istruzione "INT AUTO_INCREMENT PRIMARY KEY" che inserirà un numero univoco per ogni record. A partire da 1 e aumentato di uno per ogni record.

###########################################################################################################################################################

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

###########################################################################################################################################################

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY") #Se la tabella esiste già, utilizzare la parola chiave ALTER TABLE
#Crea chiave primaria su una tabella esistente: