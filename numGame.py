#game rules:
#The game should ask for a number
#El programa te dirá si el número a adivinar es mayor o menor que el número introducido
#El juego te dará tres oportunidades para adivinar.
#Cuando se acaben los intentos, el juego mostrará "GAME OVER"
#En caso que adivines el número, el juego mostrara "WINNER"

def game(secretNum, tries):
	triesNum = 1
	num = int(input("write a number between 1 to 5 "))

	while (secretNum != num) & (triesNum < tries):
		if(secretNum > num):
			print("the secret number is greater")
		else:
			print("the secret number is lower")
		num = int(input("write a number again "))
		triesNum = triesNum + 1
	return triesNum

def score(triesNum, tries):
	if(triesNum < tries):
		print("***********")
		print("W I N N E R")
		print("***********")
	else:
		print("****************")
		print("G A M E  O V E R")
		print("****************")

import random
secretNum = random.randint(1,5)
tries = 3
triesNum = game(secretNum, tries)
score(triesNum, tries)
