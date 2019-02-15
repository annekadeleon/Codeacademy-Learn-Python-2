#from random module import randint function
from random import randint

#empty list called board
board = []

#iterates 5 times
for i in range(5):
	#adds a new list to board with value "0" * 5
	board.append(["0"] * 5)

#function print_board take one argument board
def print_board(board):
	#for each list in list board
	for row in board:
			#prints values joined by a space
			print " ".join(row)

#runs print_board function with input board
print_board(board)

#function random_row takes one argument board
def random_row(board):
	#returns a random integer from 0 to (length of board - 1)
	return randint(0, len(board) - 1)

#function random_col takes one argument board
def random_col(board):
	#returns a random integer from 0 to (length of first list in board - 1)
	return randint(0, len(board[0]) - 1)

#variable ship_row initiated with result of random_row function with input board 
ship_row = random_row(board)
#variable shio_col initiated with result of random_col function with input board
ship_col = random_col(board)

"""print ship_row
print ship_col"""

#iterates 4 times
for turn in range(4):
	#prints Turn 1 then increments when loop starts over until 4
	print("Turn"), (turn + 1)
	#variable guess_row initiated with integer input of user
	guess_row = int(raw_input("Guess Row: "))
	#variable guess_col initiated with integer input of user
	guess_col = int(raw_input("Guess Col: "))
	
	#if user's guesses are equal to both ship_row and ship_col
	if ((guess_row == ship_row) and (guess_col == ship_col)):
		#they win the game
		print("Congratulations! You sank my battleship!")
		#programme ends
		break
	#if user's guesses are not equal to both ship_row and ship_col
	else:
		#if any of user's guesses are less than 0 or more than 5
		if ((guess_row not in range(5)) or (guess_col not in range(5))):
			print("Oops, that's not even in the ocean.")
		#if the position of user's guess is "X"
		elif (board[guess_row][guess_col] == "X"):
			print("You guessed that one already.")
		else:
			print("You missed my battleship!")
			#reassigns value of position of user's guess to "X"
			board[guess_row][guess_col] = "X"
			#if the loop has iterated 3 times
			if (turn == 3):
				print("Game Over")

#runs function print_board with input board
print_board(board)
