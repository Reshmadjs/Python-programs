import mysql.connector
dataBase=mysql.connector.connect(
host="localhost",
user="root",
passwd="D!lshad4149",
database="project"
	)

cursorObject=dataBase.cursor()
sql="INSERT INTO STUDENT(NAME,BRANCH,ROLL,SECTION,AGE) VALUES(%s,%s,%s,%s,%s)"
val=("dilshad","cs","7","A","26")

cursorObject.execute(sql,val)
dataBase.commit()
dataBase.close()