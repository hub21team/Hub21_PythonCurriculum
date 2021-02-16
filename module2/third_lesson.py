
dct = {"Ece": {"name":"Ece","surname":"Azizoglu","age":22,"gender":"female"},
	   "Haldun": {"name":"Haldun","surname":"Balim","age":22,"gender":"male"},
	   "Tanalp": {"name":"Bob","surname":"Sengun","age":21,"gender":"male"}}

def welcome(dct,key):
	name = dct[key]["name"]
	surname = dct[key]["surname"]
	print(name,surname,"welcomes you")


def canDrive(dct,key):
	return dct[key]["age"] > 18

def print_person(dct,key):
	print("my name is",dct[key]["name"],dct[key]["surname"])
	print("I am",dct[key]["age"],"years old")


def birthdat(dct,key):
	dct[key]["age"] += 1


welcome(dct,"Ece")
welcome(dct,"Haldun")
welcome(dct,"Tanalp")





class Person:
	def __init__(self,name,surname,age,gender):
		self.name = name
		self.surname = surname
		self.age = age
		self.gender = gender


	def welcome(self):
		print(self.name,self.surname,"welcomes you")


	def canDrive(self):
		return self.age>18

	def __repr__(self):
		st = "my name is "+ self.name + " " + self.surname + "\n"
		st += "I am " + self.age + " years old"+"\n"
		return st

	def birthday(self):
		self.age += 1


ece = Person("Ece","Azizoglu",22,"female")
haldun = Person("Haldun","Balim",22,"male")
tanalp = Person("Tanalp","Sengun",21,"male")

ece.welcome()
haldun.welcome()
tanalp.welcome()

print(ece)
print(haldun)
print(tanalp)

