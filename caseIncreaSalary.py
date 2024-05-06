x = int(input("How much is your salary? ")) #salary
y = int(input("what is your category' number? 1/2/3/4 ")) #category

if y == 1:
	x1 = x * 1.15;
	print("your category number 1 has a new salary", x1) 
elif y == 2:
	x2 = x * 1.1;
	print("your category number 2 has a new salary", x2)
elif y == 3:
	x3 = x * 1.08;
	print("your category number 3 has a new salary", x3)
elif y == 4:
	x4 = x * 1.07;
	print("your category number 4 has a new salary", x4)
else:
	print("wrong choice")
