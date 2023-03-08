import mysql.connector
 
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Animali"
)
 
mycursor = mydb.cursor()
 
mycursor.execute("CREATE TABLE Mammiferi2 (PersonID int AUTO_INCREMENT PRIMARY KEY, Nome_proprio varchar(255), Razza varchar(255), Peso int, Eta int)")




