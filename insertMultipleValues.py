import mysql.connector
dataBase=mysql.connector.connect(
host="localhost",
user="root",
passwd="D!lshad4149",
database="project"
	)

cursorObject=dataBase.cursor()
# sql="INSERT INTO STUDENTS (NAME,BRANCH,ROLL,SECTION,AGE) VALUES(%s, %s, %s, %s, %s)"
# val=val = [("Nikhil", "CSE", "1", "A", "18"),
#        ("Nisha", "CSE", "2", "A", "18"),
#        ("Rohan", "MAE", "3", "B", "20"),
#        ("Amit", "ECE", "4", "A", "21"),
#        ("Anil", "MAE", "5", "B", "20"),
#        ("Megha", "ECE", "6", "A", "22"),
#        ("Sita", "CSE", "7", "A", "19")]
# cursorObject.executemany(sql,val)
# dataBase.commit()

# sql="ALTER TABLE EMPLOYEE RENAME COLUMN ROLL TO EMP_NO"
# cursorObject.execute(sql)



sql="INSERT INTO EMP(NAME,BRANCH,EMP_NO,SECTION,AGE, ROLL) VALUES(%s, %s, %s, %s, %s,%s)"
val=val = [("dillu", "Soft eng", "70", "C", "30",1),
       ("pillu", "something", "65", "D", "35",2),
       ("chillu", "Bed", "40", "E", "40",3),
       ("tillu", "Med", "30", "F", "45",3),
       ("killu", "police", "35", "G", "25",3),
       ("millu", "nurse", "55", "H", "27",2),
       ("ellu", "lawyer", "60", "I", "50",1)]


cursorObject.executemany(sql,val)
dataBase.commit()
dataBase.close()       