import mysql.connector
dataBase=mysql.connector.connect(
host="localhost",
user="root",
passwd="D!lshad4149",
database="project"
	)

cursorObject=dataBase.cursor()

studentRecord=""" CREATE TABLE EMP(
                  NAME VARCHAR(20) NOT NULL,
                  BRANCH VARCHAR(50),
                  EMP_NO INT  PRIMARY KEY,
                  SECTION VARCHAR(5),
                  AGE INT,
                  ROLL INT,
                  FOREIGN KEY (ROLL) REFERENCES STUDENTS(ROLL)
) """



cursorObject.execute(studentRecord)

dataBase.close()