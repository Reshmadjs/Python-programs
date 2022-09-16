a,b,c=[int(x) for x in input("enter three values").split()]
if ((a > b and a < c) or (a<b and a>c)):
	print("%d is between %d and %d" % (a,b,c))
	
elif ((b>c) and (b<a)) or ((b<c) and (b>a)):
	print("{} is between {} and {}".format(b,a,c))
elif ((c>a) and(c<b)) or ((c<a) and (c>b)):
	print("{} is between {} and {}".format(c,a,b))



