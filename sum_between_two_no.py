x,y=[int(x) for x in input("enter numbers").split()]
sum=0
for i in range(x,y+1):
	sum=sum+i

print("sum={}".format(sum))	