import random
import os

def wordchoice():
  wordlist = []

  here = os.path.dirname(os.path.abspath(__file__))
  filepath = os.path.join(here, 'Woordlijst.txt')
  with open(filepath, "r") as words:
    for line in words:
      wordlist.append(line.strip())
  # print(wordlist)
  return random.choice(wordlist)

word = wordchoice()
# print(word)
wordLength = len(word)
currentState = "_" * wordLength
currentState = list(currentState)
guessedLetters = []
correctGuess = False
failedGuesses = 0
hangingMan = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========''', '''
  +---+
  |   |
  O   |
 |||  |
 | |  |
      |
=========''', '''
  +---+
      |
      |
  O   |
 /|\\  |
 / \\  |
=========''']

while True: # gameplay loop
	print("\n")
	guess = input("Guess a letter or word: ")

	if guess in guessedLetters: print("Already guessed that!")
	elif len(guess)==1: #guessing a letter
		guessedLetters.append(guess)
		guessedLetters.sort()
  
		for i in range(wordLength):
			if guess == word[i]:
				currentState[i]=guess
				print("You got a letter!!")
				correctGuess=True
		if correctGuess==False:
			print("That letter was not in the word! Womp womp")
			failedGuesses += 1
	elif len(guess)>1: # guessing a word??
		print("Can't guess words... Yet??") 

	print("".join(currentState))
	print("Guessed letters: {}".format(guessedLetters))

	if 0 < failedGuesses < 8: # drawing the hangman
		print(hangingMan[failedGuesses-1])
	elif failedGuesses >= 8: #fail condition
		print(hangingMan[7])
		print("You dead... Game Over")
		break
	elif word == "".join(currentState): # win condition
		print(hangingMan[8])
		print("OMG you did it! You WON!")
		break

	correctGuess=False # reset correct guess bool


'''
capitalize guessed letters
guessing words
7/8 bij win/lose conditions weg
restart
more words
show correct word on game over
def Main and everything in functions

difficulty. 999 oid cheat code
'''
