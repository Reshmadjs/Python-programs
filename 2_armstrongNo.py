# findin armstrong number
import numpy as np
a=int(input("enter number"))

x=[int(x) for x in str(a)]
print(x)
sum=0
for i in np.power(x,3):
	
	sum=sum+i
if np.equal(sum,a):
	print("armstrong of number {} is {}".format(a,sum))	
else:
	print("{} is not armstrong number".format(a))

y=a
y=np.power(y,3)

print("cube of y is ",y)



