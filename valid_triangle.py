a,b,c=[int(x) for x in input("enter three numbers").split()]
if (a+b)>c and (b+c)>a and (a+c)>b:
	print("traingle is valid")
else:
	print("traingle is not valid")
