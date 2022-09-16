x,n=[int(x) for x in input("enter x and n").split()]
def power(x,n):
	if n==1:
		return x
	return x*power(x,n-1)

print(power(x,n))	