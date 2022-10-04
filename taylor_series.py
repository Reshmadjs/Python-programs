# Write a function power, which calculates x . Write another function, which calculates n! Using
# for loop. Use these functions to calculate the sum of first n terms of the Taylor series
sum=0
def factorial(power):
	fact=1
	while(power):
		fact=fact*power
		power=power-1
	return fact

def powers(n,power):
	mult=1
	while(power):
		mult=mult*n
		power=power-1
	return mult	
	
n,power,val=[int(x) for x in input("enter value and its raised to the power and how many time").split()]
# ans=powers(n,power)
# print(ans)

# print("factorial is {}".format(factorial(power)))

for i in range(3,val*2):
	if (i/2 == 0):
		next
	sum=sum+(powers(n,i))/factorial(i)
	# i=i+2

print("sum is {}".format(sum))	
