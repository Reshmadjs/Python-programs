# 1/x  +  2/x^2  + 3/x^3 .....

x,n=[int(x) for x in input("enter x and n value").split()]
sum=0

def power(x,n):
	mult=1
	for i in range(1,n+1):
		mult=mult*x
	return mult


print(power(x,n))		
	

for i in range(1,n+1):
	sum=sum+(i/power(x,i))

print(sum)	
