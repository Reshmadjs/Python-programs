a,b,c,d=[int(x) for x in input("enter first fraction a and b then second fraction c and d").split()]
def plus(a,b,c,d):
	numerator=(a*d)+(c*b)
	denominator=b*d
	print("fraction is {}/{}".format(numerator,denominator))

def minus(a,b,c,d):
	numerator=(a*d)-(c*b)
	denominator=b*d
	print("fraction is {}/{}".format(numerator,denominator))

def mult(a,b,c,d):
	numerator=a*c
	denominator=b*d
	print("fraction is {}/{}".format(numerator,denominator))	

choice=int(input("enter choice"))
if choice==1:
	plus(a,b,c,d)

elif choice==2:
	plus(a,b,c,d)

elif choice==3:
	plus(a,b,c,d)

else:
	print("wrong choice")			