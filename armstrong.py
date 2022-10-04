# All armstrong numbers between two numbers


def cube(a):
	result=a*a*a
	return result


a,b=[int(x) for x in input("enter two numbers").split()]

def recur(n):
		if n!=0:
			rem=n%10
			result1=cube(rem)
			# print(rem)
			result2= recur(int(n/10))+result1
			return result2
		return 0




for i in range(a,b+1):
	if recur(i)==i:
		print("{} is armstrong number".format(i))
	
