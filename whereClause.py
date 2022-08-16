import mysql.connector
  
dataBase = mysql.connector.connect(
  host ="localhost",
  user ="root",
  passwd ="D!lshad4149",
  database = "project"
)
 
# preparing a cursor object
cursorObject = dataBase.cursor()

query="SELECT * FROM STUDENT WHERE AGE>20"

cursorObject.execute(query)
result=cursorObject.fetchall()
for x in result:
  print(x)

dataBase.close()  
