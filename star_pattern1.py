# row,col=[int(row) for row in input("how many rows and columns you want").split()]
# def func(row,col):
# 	for i in range(0,row):
# 		for x in range(0, (row-i)*2):
# 					print(" ", end = "")
# 		for j in range(0,col):
# 			if(i>=j):
# 				print("*", end="")
# 				for x in range(0, row):
# 					print(" ", end = "")
# 		print("\n")		

# func(row,col)		
			

row,col=[int(row) for row in input("how many rows and columns you want").split()]
def func(row,col):
	for i in range(0,row):
		
		for x in range(0,(row-i)):
			
			print(" ", end = " ")


					
		for j in range(0,col):
			if(i>=j):
				print("*", end="")
				print(" ", end=" ")
				
		print("\n")		

func(row,col)		
