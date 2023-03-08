import mysql.connector
 
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Animali"
)
mycursor = mydb.cursor()

for i in range(5): # ripetiamo il ciclo 5 volte
 # chiediamo all'utente di inserire i dati per un nuovo animale
    nome = input("Inserisci il nome proprio dell'animale: ")
    razza = input("Inserisci la razza dell'animale: ")
    peso = float(input("Inserisci il peso dell'animale: "))
    eta = int(input("Inserisci l'età dell'animale: "))
    sql = "INSERT INTO Mammiferi2 (  Nome_proprio , Razza , Peso , Eta ) VALUES ( %s, %s, %s, %s)"
    val =  ( nome, razza, peso, eta)
    mycursor.execute(sql, val)

mydb.commit()


print(mycursor.rowcount, "was inserted.")