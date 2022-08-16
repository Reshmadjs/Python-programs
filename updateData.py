import mysql.connector
  
dataBase = mysql.connector.connect(
  host ="localhost",
  user ="root",
  passwd ="D!lshad4149",
  database = "project"
)
 
# preparing a cursor object
cursorObject = dataBase.cursor()

query="UPDATE STUDENT SET AGE=27 WHERE name='dilshad'"

cursorObject.execute(query)
dataBase.commit()
 
# disconnecting from server
dataBase.close()