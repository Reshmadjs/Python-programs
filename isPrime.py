n=int(input("enter the number"))


def is_prime(n):
	i=2
	while(i<n):
		
		if n==2:
			return True	
		elif(n%i)==0:
			return False
		
		i+=1	
	return True

	
	
		
			
print(is_prime(n))
			
			
		