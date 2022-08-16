#Defining instance variable using constructor
# class Dog:
#   animal="dog"
#   def __init__(self,breed,color):
#     self.breed=breed
#     self.color=color

# rodger=Dog("pug","brown")
# buzo=Dog("bulldog","white")

# print("-----Rodger details-----")
# print("rodger is a",rodger.animal)
# print("rodger is ",rodger.breed)
# print("rodger is a "+ rodger.color+ "coloured dog")

# print("-----Buzo details-------")
# print("buzo is a",buzo.animal)
# print("buzo is a",buzo.breed)
# print("buzo is a "+buzo.color+ " coloured dog") 


#--------------------------------------------------------------------------

#Defining instance varibale using normal method

class Dog:
  animal="dog"
  def __init__(self,breed):
    self.breed=breed

  def setColor(self,color):
    self.color=color

  def getColor(self):
    return self.color



rodger=Dog("pug")
rodger.setColor("brown")
print (rodger.getColor())   


