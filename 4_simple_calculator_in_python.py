def add(x,y):
	result=x+y
	print(x ,"+",y,"=",result)

def sub(x,y):
	result=x-y
	print(x ,"-",y,"=",result)

def mult(x,y):
	result=x*y
	print(x ,"*",y,"=",result)

def div(x,y):
	result=x/y
	print(x ,"/",y,"=",result)

print("select choices")
choice=int(input("1.add 2.sub 3.mult 4.div"))
x,y=[int(x) for x in input("enter two numbers").split()]
if choice==1:add(x,y)
elif choice==2:sub(x,y)
elif choice==3:mult(x,y)
else:
	div(x,y)







