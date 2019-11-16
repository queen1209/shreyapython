from gameFunctions import gameVars

# what are you trying to compare insie this function?
# you will need to pss those things in as arguments
# inside the round brackets
def comparechioces(thing1, thing2):
	if player.lower() == "quit":
		exit()
	elif gameVars.computer == player:
		print("tie! no one wins, play again")

	elif player.lower() == "rock":
		if gameVars.computer == "paper":
			print("you lose!", gameVars.computer, "covers", player, "/n")
			gameVars.player_lives = gameVars.player_lives - 1
		else:
			print("you win!", player, "smashes", gameVars.computer, "/n")
			gameVars.computer_lives = gameVars.computer_lives - 1

	elif player.lower() == "paper":
		if gameVars.computer == "scissors":
			print("you lose!", gameVars.computer, "cuts", player, "/n")
			gameVars.player_lives = gameVars.player_lives - 1
		else:
			print("you win!", player, "covers", gameVars.computer, "/n")
			gameVars.computer_lives = gameVars.computer_lives - 1

	elif player.lower() == "scissors":
		if gameVars.computer == "rock":
			print("you lose!", gameVars.computer, "smashes", player, "/n")
			gameVars.player_lives = gameVars.player_lives - 1
		else:
			print("you win!", player, "cuts", gameVars.computer, "/n")
			gameVars.computer_lives = gameVars.computer_lives - 1

	else:
		print("That's not a valid choice, try again")