import mysql.connector
dataBase=mysql.connector.connect(
host="localhost",
user="root",
passwd="D!lshad4149",
database="project"
	)

cursorObject=dataBase.cursor()

studentRecord=""" CREATE TABLE STUDENTS (
                  NAME VARCHAR(20) NOT NULL,
                  BRANCH VARCHAR(50),
                  ROLL INT PRIMARY KEY,
                  SECTION VARCHAR(5),
                  AGE INT
) """



cursorObject.execute(studentRecord)

dataBase.close()