# col=int(input("how many cols u want"))
# count=1
# row=col
# for i in range(65,90+1):
# 	col=col-1
# 	print(" ")
# 	for j in range():
# 		while(count<=col):
# 			print(chr(i),end=" ")
# 			count=count+1
		
			
		
			
	

array = ['a','b','c','d','e','f', 'g', 'h', 'i', 'j', 'k', 'l','m','n','o','p','q', 'r', 's']

col = int(input("how many col:"))
count = 0
for r in range(0, col+1):
	for c in range(0, col-r):
		try:
			print(array[count],end=" ")
			count +=1
		except:
			print('$',end=" ")
	print("")