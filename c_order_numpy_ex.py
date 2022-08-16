import numpy as np
a=np.arange(0,12)
print("original array:",a)
a=a.reshape(3,4)
print("after reshaping array is",a)
print("Iteration")

# for x in np.nditer(a,flags = ['external_loop'],order='C'):
	
# 	print(x)
	

it=np.nditer(a,flags=['f_index'])
while not it.finished:
	print("%d <%d>" % (it[0],it.index),end="")
	it.iternext()









