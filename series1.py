# x+3x+5x+7x....

x,n=[int(x) for x in input("enter x and n value").split()]
sum=0
for i in range(1,n*2):
	if i%2!=0:
		sum=sum+(i*x)

print(sum)		