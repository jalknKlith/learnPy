#first number
x = int(input("first number "))
#second number
y = int(input("second number "))
#operator
z = input("operator: +, -, * or / ")

if z == "+":
	print(x+y)
elif z == "-":
	print(x-y)
elif z == "*":
	print(x*y)
elif z == "/":
	print(x/y)
else:
	print("wrong choice")
