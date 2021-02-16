# primer 1
def func(x):
	x = x*2

x = 2
func(x)
print(x)

# primer 2
def f1(x):
	return x*2

def f2(x):
	return x*3

def f3(x):
	return f1(x) + f2(x)

# primer 3
sm = 0
for i in range(5):
	sm += i


sm = 0
for i in range(10):
	sm += i


def func(x):
	sm = 0
	for i in range(x):
		sm += i
	return sm

func(5)
func(10)

# mc 1

def func(x,y,z):
	return 10*x+8*y+5*z

# mc 2

def isPalindrome(st):
	for i in range(len(st)//2):
		if st[i] != st[-i]:
			return False
	return True

# mc 3

def isPrime(x):
	for i in range(1,int(x**0.5)+1):
		if x%i ==0:
			return False
	return True


# mc 4

def swap(ls,i,j):
	temp = ls[i]
	ls[i] = ls[j]
	ls[j] = temp

# mc 5 (hard)

def bubble_sort(ls):
	while True:
		did_change = False
		for i in range(len(ls)-1):
			if ls[i]>ls[i+1]:
				swap(ls,i,i+1)
				did_change = True
		if not did_change:
			break

	return ls





