import numpy as np

lst=[]
n=int(input("enter how many values"))
for i in range(0,n):
	inputs=(int(input("enter no")))
	lst.append(inputs)

print(lst)

result=np.sum(lst)
print(result)	