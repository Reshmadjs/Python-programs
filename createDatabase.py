import mysql.connector
dataBase=mysql.connector.connect(
host="localhost",
user="root",
passwd="D!lshad4149"
	)

cursorObject=dataBase.cursor()
cursorObject.execute("CREATE DATABASE project")