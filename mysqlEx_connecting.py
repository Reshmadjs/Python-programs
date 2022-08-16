# We can connect to the MySQL server using the connect() method. 

import mysql.connector
dataBase=mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="D!lshad4149"
	)

print(dataBase)
dataBase.close()