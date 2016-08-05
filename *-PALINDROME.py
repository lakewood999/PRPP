#ACSL PALINDROME 2001-2002 Contest #3

#Detects whether a number is a palindrome
def ispalindrome(x):
	global palindrome
	x = str(x)
	#print(x)
	if len(x) == 1:
		palindrome = "True"
	else:
		length = len(x)
		if length/2 == 0:
			length = length
		else:
			length = length-1
		totaltimes = length/2
		times = 0
		first = 0
		last = length
		palindrome = ""
		while times < totaltimes:
			#print(x[first])
			#print(x[last])
			if x[first] == x[last] and palindrome != "False":
				palindrome = "True"
			else:
				palindrome = "False"
			first += 1
			last -= 1
			times += 1
	return palindrome
	#print(palindrome)

#Adds a number to it's reverse self
def add(x):
	y = ""
	x = str(x)
	length = len(x)
	times = 0
	end = length-1
	while times < length:
		y += x[end]
		end -= 1
		times += 1
	x = int(x)
	x += int(y)
	return x

#Main program that puts things together
def main(usin,num):
	if ispalindrome(usin) == "True":
		out = num+str(usin)
	else:
		addtimes = 1
		while ispalindrome(usin) == "False" and addtimes < 11:
			usin = add(usin)
			#print(addtimes,usin)
			addtimes += 1
			#print(x)
		
		#print(ispalindrome(usin))
		addtimes -= 1
		if ispalindrome(usin) == "True":
			out = num+str(usin)
		if addtimes == 10:
			out = num+"NONE, "+str(usin)
	return out

#Inputs
a = main(input("1. "), "1. ")
b = main(input("2. "), "2. ")
c = main(input("3. "), "3. ")
d = main(input("4. "), "4. ")
e = main(input("5. "), "5. ")

#Line breaks
print()

#Outputs
print(a)
print(b)
print(c)
print(d)
print(e)

	
	
	
	
	
