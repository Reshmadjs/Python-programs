import mysql.connector

dataBase=mysql.connector.connect(
host="localhost",
user="root",
passwd="D!lshad4149",
database="project"
	)

cursorObject=dataBase.cursor()

query=" SELECT * FROM STUDENT ORDER BY NAME DESC"
cursorObject.execute(query)

result=cursorObject.fetchall()

for x in result:
	print(x)

dataBase.close()	
