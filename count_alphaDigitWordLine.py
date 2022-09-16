character,word,line=0,0,0
print("enter chars")
while True:
	ch=input()
	if ch!='*':
		if ch!=' ' or ch!='\n':
			character+=1
		if ch=='\t':
			word=word+1
		if ch=='\n':
			line=line+1
	else:
		print(ch.count('\n'))
		print("no of characters are :{}, no of words are {} and no of lines are {}" .format(character,word,line))

