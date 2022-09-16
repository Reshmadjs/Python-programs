a,b=[int(x) for x in input("enter two variables").split()]
operator=input("enter operators to perform operations")
if operator=='+':
	print(a+b)
elif operator=='-':
	print(a-b)
elif operator=='*':
	print(a*b)
elif operator=='/':
	print(a/b)
else:
	print("incorrect operator")				