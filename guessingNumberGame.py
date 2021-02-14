import random
winningNumber = random.randint(1,100)
guess = 1
num = int(input("Enter a number 1 to 100 : "))
gameOver = False
while not gameOver:
	if num == winningNumber:
		print(f"You win, and you gussed in {guess} times.")
		gameOver = True
	else:
		if num < winningNumber:
			print("Too Low.")
		else:
			print ("Too High.")
		guess += 1
		num = int(input("Guess Again : "))


