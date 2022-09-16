n=int(input("enter number"))

def rev(n):
	if n==0:
		return ""
	else:	
		rem=n%10
		final=rev(int(n/10))+ str(rem)
		# print("final is", final)
		return final

if rev(n)==(str(n)[::-1]):
	print("yes")
else:
	print("no")	
