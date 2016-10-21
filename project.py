import time

name = input("What is your name?")
print("Hello,"+ name,"Time to play")

#Wait for 1 second
time.sleep(1)

print("Start guessing...")
time.sleep(0.5)

#here we set the secret word
word = "secret"

#Create a variable with an empty value
guesses = ""

#determine number of turns
turns = 10

#check if the turns are more than zero
while(turns > 0):

	#make a counter that starts with zero
	failed = 0

	#for every charcter in secret_word not found
	for char in word :

		#see if the character is in the player's guess
		if char in guesses:
			print(char)
		else : 
			#if not found,print dash
			print("_")

			failed += 1


	if failed == 0:
		print ("You won")
		break

	guess = input("guess a character:")

	#set the players guess to guesses
	guesses += guess

	#if the guess is not found in the secret word
	if guess not in word :

		#turns counter decreases with 1
		turns -= 1

		print("Wrong")

		#how many turns are left
		print("You have",+ turns, "more guesses")

		#if the turms are equal to zero
		if turns == 0:
			print("You lose")