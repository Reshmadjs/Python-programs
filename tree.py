class Node:
	def __init__(self,value):
		self.left=None
		self.data=value
		self.right=None


class Tree:
	def CreateNode(self,data):
		return Node(data)


	def insert(self,node,data):
		if node is None:
			return self.CreateNode(data)

		if 	data<node.data:
			node.left=self.insert(node.left,data)


		else:
			node.right=self.insert(node.right,data)

		return node

	def traverse(self, root):
		if root is not None:
			self.traverse(root.left)
			print(root.data)
			self.traverse(root.right)	


tree=Tree()
root=tree.CreateNode(5)

tree.insert(root,2)
tree.insert(root,10)
tree.insert(root,4)
tree.insert(root,1)
tree.insert(root,9)
tree.insert(root,8)
tree.insert(root,4)
tree.insert(root,3)
tree.insert(root,6)
tree.insert(root,7)



tree.traverse(root)		



