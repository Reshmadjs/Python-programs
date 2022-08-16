import numpy as np
a=np.array([9,3,1,7,4,3,6])
b=np.argsort(a)
c=np.zeros(len(b),dtype=int)
for i in range(0,len(b)):
	c[i]=a[b[i]]

print(c)	