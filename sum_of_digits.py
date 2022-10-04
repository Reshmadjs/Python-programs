n=int(input("enter digit"))

sum=0
def digit(n):
	global sum
	if n==0:
		return 0
	else:
			
		rem=n%10
		sum=sum+rem
		addition=digit(int(n/10))
	return sum

print(digit(n))	