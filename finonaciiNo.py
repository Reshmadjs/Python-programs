n=int(input("enter  how many numbers"))
a=0
b=1
c=a+b
print(b,c,end='\n')
for i in range(n):
	a=b
	b=c
	c=a+b
	print(c)
