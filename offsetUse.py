import mysql.connector
  
dataBase = mysql.connector.connect(
  host ="localhost",
  user ="root",
  passwd ="D!lshad4149",
  database = "project"
)
 
# preparing a cursor object
cursorObject = dataBase.cursor()

query = "SELECT * FROM STUDENT LIMIT 2 OFFSET 3"

cursorObject.execute(query)
   
myresult = cursorObject.fetchall()
   
for x in myresult:
    print(x)
 
# disconnecting from server
dataBase.close()