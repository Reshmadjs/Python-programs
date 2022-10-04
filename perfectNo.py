a,b=[int(x) for x in input("enter two numbers").split()]
sum=0
for i in range(a,b+1):
	sum=0
	for j in range(1,i):
		if i%j==0:
			sum=sum+j
	if sum==i:
		print("{} is perfect number".format(i))

