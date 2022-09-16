x,y=[int(x) for x in input("anter two numbes of a point").split()]
if x<0 and y>0:
	print("point lies in first quadrant")
elif x>0 and y>0:
	print("point lies in second quadrant")
elif x<0 and y<0:
	print("point lies in third quadrant")
else:
	print("point lies in fourth quadrant")
