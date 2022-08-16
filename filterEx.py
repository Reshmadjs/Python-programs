def func(variable):
	letters=['a','e','i','o','u']
	if(variable in letters):
		return True
	else:
		return False

sequence=['a','b','c','d','e','i','r','d']
filtered=filter(func,sequence)

for s in filtered:
	print(s)

		