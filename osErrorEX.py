import os
try:
	filename="deco.py"
	file=open(filename,"r")
	text=file.read()
	file.close()
except IOError:
	raise Exception("file doesnt exist")




