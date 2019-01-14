from random import randint

#Generates a random number between and including 1 to 10
random_number = randint(1, 10)

#Player's "lives"
guesses_left = 3

while guesses_left > 0:
	guess = int(raw_input("Your guess: "))
	if guess == random_number:
		print("You win!")
		break
	else:
		guesses_left -= 1
else:
	print("You lose.")
