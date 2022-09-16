def area_of_circle():
	radius=float(input("enter radius"))
	ans=3.14*radius*radius
	print("area of circle is{}".format(ans))

def circumference_of_circle():
	radius=float(input("enter radius"))
	ans=2*3.14*radius
	print("cirumference of circle is{}".format(ans))

def volume_of_sphere():
	radius=float(input("enter radius"))
	ans=(4/3)*3.14*radius*radius*radius
	print("volume of sphere is{}".format(ans)) 	

n=int(input("enter choices: 1.area_of_circle 2.circumference_of_circle 3.volume_of_sphere"))
if n==1:
	area_of_circle()
elif n==2:
	circumference_of_circle()
elif n==3:
	volume_of_sphere()
else:
	print("wrong choice")			