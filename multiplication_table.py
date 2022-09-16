start, end, limit=[int(x) for x in input("enter __To__ table and how many multiples u want").split()]

for row in range(start,end+1):
	print(" ")
	for col in range(1,limit+1):
		print("{} * {} = {}   |  ".format(row,col+1,(row*col)), end=' ')
