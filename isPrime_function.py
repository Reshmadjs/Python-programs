# Write a function isPrime, which accepts an integer as parameter and returns 1 if the number
# is prime and 0 otherwise. Use this function in main to display the first 10 prime numbers

def isPrime(n):
	
	for i in range(1,n+1):
		count=0
		for j in range(1,i+1):
			if i%j==0:
				count+=1
		if count==2:
			print("{} is prime no".format(i))	
		
		
	
			


n=int(input("enter number till u want prime no"))
isPrime(n)		

		