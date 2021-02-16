# primer
dct = {"anne":51,"baba":55,"abi":12}


# primer 2
colors = ("red","blue","green")
colors_ls = ["red","blue","green"]


# mc 1
prices_dct = ["banana":2, "apple":1, "kale":3]
stocks = ["banana":4,"apple":2,"kale":5]
total_price = 0
for item in prices_dct:
	total_price += prices_dct[item] * stocks[item]



# mc 2
dct = {"kırmızı":"red", "elbise":"dress", "çok":"very", "güzel":"beautiful"}
tr_text = "kırmızı elbise çok güzel"
eng_text = []
for word in tr_text.split():
	eng_text.append(dct[word])
eng_text = " ".join(eng_text)

# mc 3
ls = [1,2,3,4,1,2,3,4,1,2,3,4]
unique = []
for el in ls:
	if el in unique:
		continue
	unique.append(el)


unique = set(ls)
unique.add(2)
unique.remove(2)

# mc 4
dct = {"France":"Paris","Turkey":"Istanbul"}
while True:
	ct = input("Enter a country: ")
	if ct not in dct:
		capital = input("Enter the capital of",ct)
		dct[ct] = capital
	print(dct[ct])




# big challenge
actors_dct = ["mov1":["act1","act2"], "mov2":["act1","act3"]]

# given an actor name find how many movies did he play in

# given two actor names find movies that they both play in

# given 


