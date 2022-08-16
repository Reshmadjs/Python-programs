import mysql.connector
  
# Connecting to the database
mydb = mysql.connector.connect(
  host ='localhost',
  database ='project',
  passwd ="D!lshad4149",
  user ='root',
)
  
cs = mydb.cursor()
 

statement ="SELECT STUDENTS.ROLL, STUDENTS.NAME,EMP.NAME FROM STUDENTS JOIN EMP ON STUDENTS.ROLL=EMP.ROLL"
 
cs.execute(statement)
result_set = cs.fetchall()
 
for x in result_set:
    print(x)