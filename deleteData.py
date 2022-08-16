import mysql.connector

dataBase = mysql.connector.connect(
  host ="localhost",
  user ="root",
  passwd ="D!lshad4149",
  database="project"
  )

cursorObject = dataBase.cursor()
query = "DELETE FROM STUDENT WHERE NAME = 'Sita'"
cursorObject.execute(query)
dataBase.commit()
 
# disconnecting from server
dataBase.close()