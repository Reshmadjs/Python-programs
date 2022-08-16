def addition(n):
	return n+n

numbers=(1,2,3,4,5,6,7)
results=map(addition,numbers)
for result in results:
	print(result)
