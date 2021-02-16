

print("")
while True:
	choice = input("What will you do")
	if choice == "a" or choice=="attack":
		attack()
	elif choice == "s" or choice=="super_attack":
		super_attack()
	elif choice == "h" or choice=="heal":
		heal()