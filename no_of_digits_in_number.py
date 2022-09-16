n=int(input("enter number"))
count=0
def recursion(n):
	if n != 0:
		global count
		rem=n%10
		count=count+1
		return recursion(int(n/10))
	return ""
recursion(n)
print("{} is having {} digits in it".format(n,count))	