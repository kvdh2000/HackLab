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
print(word)
wordLength = len(word)
currentState = "_" * wordLength
currentState = list(currentState)
guessedLetters = []
correctGuess = False
failedGuesses = 0

while True:
	print("\n")
	guess = input("Guess a letter or word:")
	savestate = currentState
	if len(guess)==1:
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
	elif len(guess)>1:
		print("") # guessing a word??

	print("".join(currentState))
	print("Guessed letters: {}".format(guessedLetters))
	# switch case that draws hangman based on failedGuesses
	# check for win condition
	correctGuess=False
