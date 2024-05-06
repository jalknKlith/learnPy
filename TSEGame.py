import random 

print("TIGER, SNAKE & EAGLE")
print("ESP-Juega contra la PC elegiendo tu animal, mira las reglas:")
print("ENG-Play against the PC choosing your favorite animal, check the rules:")
print("Tiger beats Eagle")
print("Eagle beats Snake")
print("Snake beats Tiger")

x = int(input("tap a number: 1 for Tiger, 2 for Eagle or 3 for Snake "))
y = random.randint(1,3)

#player face

if x == 1:
	print("you chose Tiger")
elif x == 2:
	print("you chose Eagle")
elif x == 3:
	print("you chose Snake")
else:
	print("you passed")

#machine face

if y == 1:
	print("machine chose Tiger")
elif y == 2:
	print("machine chose Eagle")
elif y == 3:
	print("machine chose Snake")

#face to face

if x == y:
	print("D R A W")
elif x == 1 & y == 2:
	print("Y O U  W I N")
elif x == 2 & y == 3:
	print("Y O U  W I N")
elif x == 3 & y == 1:
	print("Y O U  W I N")
else:
	print("Y O U  L O S E") 
