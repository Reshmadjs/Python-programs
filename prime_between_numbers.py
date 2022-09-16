a,b=[int(x) for x in input("enter two values").split()]
count=0
for i in range(a,b+1):
	
	count=0
	for j in range(1,b):
		
		if i%j==0:
			
			count+=1
	if count==2 or i==2:
		
		print("{} is prime number".format(i))
