a,b=[int(x) for x in input("enter two numbers").split()]
if a<b:
	def max(a,b):
		for i in range(1,b):
			if a%i==0 and b%i==0:
				max=i
				
		return max
else:
	def max(a,b):
		for i in range(1,a):
			if a%i==0 and b%i==0:
				max=i
				
		return max


print(max(a,b))


