while True: 
	assign = input("Which assignment do you want to see??")

	if assign == "s": break # inputting s when asking for assignment number stops the program

	try: assign = int(assign)
	except ValueError: print("Das geen getal... pik")
	else:
		match assign:
			case 1:
				hours = input("Enter a number of hours:")

				try: hours = int(hours)
				except ValueError: print("Das geen getal... pik")
				else: print("You imput {} hours; which is {} minutes, or {} seconds".format(hours, hours*60, hours*60*60))	

			case 2:
				num = input("Input a table to multiply:")

				try: num = int(num)			
				except ValueError: print("Das geen getal... pik")
				else: 
					table = num
					i = 1

					print("{} x {} = {}".format(i, table, str(num)))
					num+=table; i+=1
					print("{} x {} = {}".format(i, table, str(num)))
					num+=table; i+=1
					print("{} x {} = {}".format(i, table, str(num)))
					num+=table; i+=1
					print("{} x {} = {}".format(i, table, str(num)))
					num+=table; i+=1
					print("{} x {} = {}".format(i, table, str(num)))
					num+=table; i+=1
					print("{} x {} = {}".format(i, table, str(num)))
					num+=table; i+=1
					print("{} x {} = {}".format(i, table, str(num)))
					num+=table; i+=1
					print("{} x {} = {}".format(i, table, str(num)))
					num+=table; i+=1
					print("{} x {} = {}".format(i, table, str(num)))
					num+=table; i+=1
					print("{} x {} = {}".format(i, table, str(num)))
			
					# en met een for loopje, omdat het kan
					# for i in range (0, 10):
					# 	print("{} x {} = {}".format(i+1, table, str(num)))
					# 	num+=table

			case 3:
				num = input("Gimme a number!")

				try: num = int(num)
				except ValueError: print("Das geen getal... pik")
				else:
					if num == 10: print("THAT's TEN")
					elif num < 10: print("Well that's a low number-")
					elif num > 10: print("Ooohhhh wow soooo big, bet you're proud of yourself huh??")
					else: print("Not a number, is it? Pik")

				month = input("Give me a month!").capitalize()
		
				match month:
					case "January" | "March" | "May" | "July" | "September" | "November": print("That Month has 31 days!")
					case "April" | "June" | "August" | "October" | "December": print("That Month has 30 days!")
					case "February": # print("That Month has... well I'm not sure, that would depend on the year... But it's either 28 or 29 days.")
						# De volgende 9 regels is om schrikkeljaren te berekenen, kan ook met de bovenstaand om dat over te slaan.
						year = input("Well to know how many days February is, I need to know what year it is")

						try: year = int(year)
						except ValueError: print("Das geen getal... pik")
						else:
							if year % 400 == 0: print(f"In the year{year}, February has 29 days!")
							elif year % 100 == 0: print(f"In the year{year}, February has 28 days!")
							elif year % 4 == 0: print(f"In the year{year}, February has 29 days!")
							else: print(f"In the year{year}, February has 28 days!")
					case _: print("No idea what you typed in, but I'm not sure it was a Month.....")
		
			case 4:
				num = input("Gimme a number")
				
				try: num = int(num)
				except ValueError: print("Das geen getal... pik")
				else:
					table = num

					for i in range (0, 10):
						print("{} x {} = {}".format(i+1, table, str(num)))
						num+=table

			case 5: 
				for i in range (101):
					if (i % 5 == 0) and (i % 7 == 0): print(f"{i}: FizzBuzz")
					elif i % 5 == 0: print(f"{i}: Fizz")
					elif i % 7 == 0: print(f"{i}: Buzz")
					else: print(i)

			case 6:
				size = input("How big do you want this arrow to be?")
				maxReached = False

				try: size = int(size)
				except ValueError: print("Das geen getal... pik")
				else:
					i = 1

					while True:
						print("@"*i)
						if i == size: 
							maxReached = True
							i-=1
						elif i == 0: break
						elif maxReached == False: i+=1
						elif maxReached == True: i-=1

				seq = input("Enter DNA sequence: ")
				newSeq = ""

				for l in seq:
					match l:
						case "A": newSeq+="T"
						case "T": newSeq+="A"
						case "C": newSeq+="G"
						case "G": newSeq+="C"
				print(newSeq)

				# de bovenstaande was hoe ik het eerst zelf wou doen. 
    		# Ik kreeg het eerst niet werkend
    		# In het googlen kwam ik het volgende tegen
				# Ze werken beide

				compSeq = str.maketrans("ATCG", "TAGC")
				print(seq.translate(compSeq))
	
			case 7:
				listNames = ["Justin", "Henk", "Jantje", "Piet", "Amelia", "Bob", "Kees", "Melle", "Sybren", "Jelly", "Nienke", "Eric", "Durk", "Jamie", "Glenn", "Corné"]

				print("Sorry snap helemaal niks van wat hier de bedoeling was. Zelfs nadat ik naar het `antwoord` gekeken heb...")

			case 8:
				listThings = ["Boeing", "Camaro", "Chevrolet", "Leeuwarden", "Kickboksen", "Kat"]
				listKeys = ["Plane", "Car Model", "Car Brand", "City", "Sport", "Animal"]
				dictThings = {}

				for i in range(len(listThings)):
					dictThings[listKeys[i]] = listThings[i]

				print(dictThings)

				Zoektocht = {'dict' : {'dict' : {'dict' : {'dict' : {'Niet deze': "Geen antwoord", 'Ook niet deze': 0, 'Nope': "Nee"}, 'list': [["bla", 15, "asdf51sf", "Hallo", ["bla", 15, "asdf51sf", "Hallo"]]], 'ding': "aaaaaaaa", 'Nog een': 15, 'nou nog eentje dan': {'Niet deze': "Geen antwoord", 'Ook niet deze': 0, 'Nope': "Nee"}}, 'list': ["bla", 15, "asdf51sf", "Hallo", ["bla", 15, "asdf51sf", "Hallo"]], 'ding': "aaaaaaaa", 'Nog een': 15, 'nou nog eentje dan': {'dict' : {'Niet deze': "Geen antwoord", 'Ook niet deze': 0, 'Nope': "Nee"}, 'list': [["bla", 15, "asdf51sf", "Hallo", ["bla", 15, "asdf51sf", "Hallo"]]], 'ding': "aaaaaaaa", 'Nog een': 15, 'nou nog eentje dan': {'Niet deze': "Geen antwoord", 'Ook niet deze': 0, 'Nope': "Nee"}}}, 'list': [["bla", 15, "asdf51sf", "Hallo", ["bla", 15, "asdf51sf", "Hallo"]]], 'ding': "aaaaaaaa", 'Nog een': 15, 'nou nog eentje dan': {'dict' : {'dict' : {'Niet deze': "Geen antwoord", 'Ook niet deze': 0, 'Nope': "Nee"}, 'list': [["bla", 15, "asdf51sf", "Hallo", ["bla", 15, "asdf51sf", "Hallo"]]], 'ding': "aaaaaaaa", 'Nog een': 15, 'nou nog eentje dan': {'Niet deze': "Geen antwoord", 'Ook niet deze': 0, 'Nope': "Nee"}}, 'list': ["bla", 15, "asdf51sf", "Hallo", ["bla", 15, "asdf51sf", "Hallo"]], 'ding': "aaaaaaaa", 'Nog een': 15, 'nou nog eentje dan': {'dict' : {'Niet deze': "Geen antwoord", 'Ook niet deze': 0, 'Nope': "Nee"}, 'list': [["bla", 15, "asdf51sf", "Hallo", ["bla", 15, "asdf51sf", "Hallo"]]], 'ding': "aaaaaaaa", 'Nog een': 15, 'nou nog eentje dan': {'dict' : {'dict' : {'Deze': "Het antwoord", 'Niet deze': "Geen antwoord", 'Ook niet deze': 0, 'Nope': "Nee"}, 'list': [["bla", 15, "asdf51sf", "Hallo", ["bla", 15, "asdf51sf", "Hallo"]]], 'ding': "aaaaaaaa", 'Nog een': 15, 'nou nog eentje dan': {'Niet deze': "Geen antwoord", 'Ook niet deze': 0, 'Nope': "Nee"}}, 'list': ["bla", 15, "asdf51sf", "Hallo", ["bla", 15, "asdf51sf", "Hallo"]], 'ding': "aaaaaaaa", 'Nog een': 15, 'nou nog eentje dan': {'dict' : {'Deze': "Het andwo0rdt", 'Niet deze': "Geen antwoord", 'Ook niet deze': 0, 'Nope': "Nee"}, 'list': [["bla", 15, "asdf51sf", "Hallo", ["bla", 15, "asdf51sf", "Hallo"]]], 'ding': "aaaaaaaa", 'Nog een': 15, 'nou nog eentje dan': {'Deze': "Het andw00rd", 'Niet deze': "Geen antwoord", 'Ook niet deze': 0, 'Nope': "Nee"}}}}}}, 'list': ["bla", 15, "asdf51sf", "Hallo", ["bla", 15, "asdf51sf", "Hallo"]], 'ding': "aaaaaaaa", 'Nog een': 15, 'nou nog eentje dan': {'dict' : {'Niet deze': "Geen antwoord", 'Ook niet deze': 0, 'Nope': "Nee"}, 'list': [["bla", 15, "asdf51sf", "Hallo", ["bla", 15, "asdf51sf", "Hallo"]]], 'ding': "aaaaaaaa", 'Nog een': 15, 'nou nog eentje dan': {'Deze': "Het andwoord", 'Niet deze': "Geen antwoord", 'Ook niet deze': 0, 'Nope': "Nee"}}}

				print(Zoektocht['dict']['nou nog eentje dan']['nou nog eentje dan']['nou nog eentje dan']['dict']['dict']['Deze'])
				print(Zoektocht['dict']['dict']['dict'])


			case 9:
				text = input("Put in some text").lower()

				if text.count("x") == text.count("o"): print("True")
				else:print("False")

			case 10: 
				words = input("Give two strings of equal length").split(" ")
				word1 = words[0]
				word2 = words[1]
				count = 0
    
				for i in range(len(word1)):
					if word1[i] == word2[i]:
						count+=1

				print(count)
    
			case 11: 
				params = input("Give three numbers").split(" ")
				x=int(params[0])
				y=int(params[1])
				n=int(params[2])        
				listNums = range(x, y+1)
				listSorted = []

				for i in listNums:
					if i % n==0:
						listSorted.append(i)
				print(listSorted)

			case 12: 
				text = input("Put in some text")
				newText = ""

				for i in text:
					newText += i
					newText += i

				print(newText)

			case _:	print("Don't have that yet, bub")
