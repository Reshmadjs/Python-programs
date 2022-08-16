# reading csv file

import csv
filename="aapl.csv"
fields=[]
rows=[]

with open(filename,'r') as csvfile:
	csvreader=csv.reader(csvfile)
	fields=next(csvreader)
	for row in csvreader:
		rows.append(row)

	print("total number of rows are:%d"%(csvreader.line_num))
	print("field names are "+",".join(field for field in fields))

	print("first 5 rows are:")
	for row in rows[:5]:
		for col in row:
			print("%10s"%col,end=" "),
			print("\n")
