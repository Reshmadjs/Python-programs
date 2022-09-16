hour,minute,seconds=[int(x) for x in input("hour:minute:seconds").split()]

if 0<=hour<24 and 0<=minute<60 and 0<=seconds<60:
	print("{}:{}:{} is valid time".format(hour,minute,seconds))
else:
	print("not valid time")
