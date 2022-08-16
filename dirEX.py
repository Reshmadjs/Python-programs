import os
directory="DirectoryEx"
parent_Dir="/home/reshma/"
path=os.path.join(parent_Dir,directory)
os.mkdir(path)
print("directoty '%s' is created" % directory)

directory="geeks"
parent_Dir="/home/reshma"
mode = 0o666
path=os.path.join(parent_Dir,directory)

os.mkdir(path,mode)
print("directory %s created" % directory)