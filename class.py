class Dog:
	animal="dog"
	def __init__(self,breed,color):
		self.breed=breed
		self.color=color

	rodger=Dog("pug","brown")
	buzo=Dog("bulldog","white")

	print("-----Rodger details-----")
	print("rodger is a",rodger.animal)
	print("rodger is ",rodger.breed)
	print("rodger is a "+ rodger.color+ "coloured dog")

	print("-----Buzo details-------")
	print("buzo is a",buzo.animal)
	print("buzo is a",buzo.breed)
	print("buzo is a "+buzo.color+ "coloured dog")	