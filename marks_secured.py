bio,maths,cs=[int(x) for x in input(" enter marks of subjects bio,maths and computer science").split()]
total=bio+maths+cs
avg=total/3
print("total marks secured is {} and average is {}%".format(total,avg))
if avg>=70:
	print("class 1")
elif 60<=avg<70:
	print("class 2")
elif 35<=avg<60:
	print(" pass class")
else:
	print("fail")		