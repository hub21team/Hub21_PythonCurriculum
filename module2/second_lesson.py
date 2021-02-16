# mc 0

def func(filename):
	with open(filename,"r") as file:
		for idx,line in enumerate(file.readlines()):
			if "waldo" in line:
				return idx



# mc 1

def func(filename):
	dct = {}
	with open(filename,"r") as file:
		for line in file.readlines():
			for word in line.split():
				if word not in dct:
					dct[word] = 0
				dct[word] += 1
	return dct


# mc 2

def func(filename):
	longest = ""
	longest_len = 0
	with open(filename,"r") as file:
		for line in file.readlines():
			for word in line.split():
				if len(word) > longest_len:
					longest_len = len(word)
					longest = word
	return longest


# mc 3
def func(filename,filenmae2):
	main_char_name = "Alice"
	my_name = "Haldun"
	lines = []
	with open(filename,"r") as file:
		for line in file.readlines():
			lines.append(line.replace(main_char_name,my_name))

	filename2 = ""
	with open(filename,"w") as file:
		file.write("\n".join(lines))


# mc 4
def func(filename):
	main_char_name = "Alice"
	my_name = "Haldun"
	lines = []
	with open(filename,"r") as file:
		for line in file.readlines():
			if "." in line:
				new_line = ""
				point = False
				for ch in line:
					if ch ==".":
						point = True
						new_line += ch
					elif point:
						point=False
						new_line += ch.upper()
			lines.append(new_line)
			else:
				lines.append(line)

	filename2 = ""
	with open(filename,"w") as file:
		file.write("\n".join(lines))


#big challenge





