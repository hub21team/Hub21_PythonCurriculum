# mc 1
num1 = int(input("What is number 1"))
num2 = int(input("What is number 2"))
if num1>num2:
	print("max is",num1)
else:
	print("max is",num2)



# mc 2 (hard)
num1 = int(input("What is number 1"))
num2 = int(input("What is number 2"))
num3 = int(input("What is number 3"))
if num1 > num2 and num1 > num3:
	print("max is",num1)
elif num2 > num3:
	print("max is",num2)
else:
	print("max is",num3)


# mc 3
weather = input("What is the weather like")
if weather == "sunny":
	print("Take sunglasses")
elif weather == "rainy":
	print("Take your umbrella")
elif weather == "snowy":
	print("Take your gloves")
else:
	print("Unknown weather",weather)



# mc 4 (ece italy)


# mc 5 (find other movies)
comedy = bool(input("Do you like comedy movies?"))
if comedy:
	print("You should watch ratatouille")
else:
	action = bool(input("Do you like action movies?"))
	if action:
		print("You should watch big hero 6")
	else:
		print("You should watch charlie and the chocolate factory")



# challenge: calculator
print("Welcome to Calculator Bot")
num1 = float(input("What is number 1"))
num2 = float(input("What is number 2"))
operation = input("What operation should I make")
if operation == "sum":
	print("Answer is",num1+num2)
elif operation == "multiplication":
	print("Answer is",num1*num2)
elif operation == "difference":
	print("Answer is",num1-num2)
elif operation == "division":
	print("Answer is",num1/num2)
else:
	print("operation",operation,"not found")


# challenge: sports
indoor = bool(input("Do you like indoor sports?"))
if indoor:
	team = bool(input("Do you like team sports"))
	if team:
		print("You should play basketball")
	else:
		print("You should play tennis")
else:
	team = bool(input("Do you like team sports"))
	ball = bool(input("Do you like sports with balls"))
	if team and ball:
		print("You should play football")
	elif team:
		print("You should play flag race")
	else:
		print("You should go swimming")



