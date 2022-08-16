
a=0
b=1

c=a+b

inputs=int(input("enter no"))

	

def fibo(inputs,b,c,a):
	print(a,b)
	print(c)
	for i in range(inputs):
		temp=b+c
		print(temp)
		b=c
		c=temp
	

fibo(inputs,b,c,a)











	
	
	




	
	

