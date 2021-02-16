# mc 1
mixed = ["banana","apple","banana","apple","potato","carrot","potato","carrot","potato","carrot"]
vegies = ["potato","carrot"]
fruits = ["banana","apple"]

v = 0
f = 0

for item in mixed:
	if item in vegies:
		v += 1
	else:
		f += 1

print("There are",v,"vegetables")
print("There are",f,"fruits")

# mc 2
st = input("Enter a string ")
for i in range(len(st)):
	print(i,st[i])


# mc 3
st = input("Enter a string ")
idx = int(input("Enter an index"))
if idx < len(st):
	print(st[idx])
else:
	print("Out of string")



# mc 4 (hard)
sm = 0
number = int(input("Enter a number "))
for digit in str(number):
	sm += str(digit)
print("Sum of digits of",number,"is",sm)



# mc 5 (hard)
st = "level"
rev = ""
for idx in range(len(st)):
	rev += st[len(st)-1-idx]


# mc 6
st = input("Enter a string ")
st = st.replace("ı","i")
st = st.replace("ü","u")
st = st.replace("ğ","g")
st = st.replace("ö","o")
st = st.replace("ç","c")
st = st.replace("ş","s")
print(st)



# challenge: 

flavors = ["chocolate","strawberry","vanilla"]
prices = [2,3,1]
order = []

print("Welcome to ice cream shop")
while True:
	fl = input("Which flavor do you want (chocolate, strawberry, vanilla, exit)")
	if fl == "exit":
		break
	elif fl in flavors:
		order.append(fl)
	else:
		print("We dont have",fl)

sm = 0
for fl in order:
	idx = flavors.index(fl)
	sm += prices[idx]
	
print("That will be",sm,"in total")



# ls = ["a","b","c","d","e"]
#  a  b  c  d  e
#  0  1  2  3  4
# -5 -4 -3 -2 -1 
# ls[2] = ?
# ls [-2] = ?
# len(ls) = 4
#for el in ls:
  #print(el)

#for i in range(0,len(ls)):
  #print(i,ls[i])


