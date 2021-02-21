"""
“Guess the Number” Game. We are going to make a “Guess
the Number” game. In this game, the computer will think of a
random number from 1 to 20, and ask you to guess the number.
You only get six guesses, but the computer will tell you if your
guess is too high or too low. If you guess the number within
six tries, you win.

"""

import random

# Initialize guess
guessesTaken = 0

# Ask for user name
print("Hello, what is your name? ")
myName = input()

# Generate a random integer
number = random.randint(1, 20)
print("Well, " + myName + ", I am thinking of a number between 1 and 20.")

# Create a while loop
while guessesTaken < 6:
	print("Take a Guess.")
	guess = int(input())
	guess = int(guess)

	guessesTaken = guessesTaken + 1

	if guess < number:
		print("Your guess is too low.")

	if guess > number:
		print("Your guess is too high.")

	if guess == number:
		break

if guess == number:
	guessesTaken = str(guessesTaken)
	print("Good job, " + myName + "!, you guessed my number in " + guessesTaken + " guesses!")

if guess != number:
	number = str(number)
	print("Nope, the number i was thinking of was " + number)
