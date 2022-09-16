n=int(input("enter number"))
def reverse(n):
	if n!=0:
		rem=n%10
		print(rem,end="")
		return(reverse(int(n/10)))
	return ""
	
reverse(n)		