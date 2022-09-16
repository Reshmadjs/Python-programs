char=input("enter character")
n=int(input("enter how many next n char u want"))
for i in range(n):
	ans=ord(char)+1
	print(chr(ans))
	char=chr(ans)
	
print("*********using recursion******************")
def rec(n,char):
	if n!=0:
		ans=ord(char)+1
		print(chr(ans))
		return rec(n-1,chr(ans))
	return ""

rec(n,char)