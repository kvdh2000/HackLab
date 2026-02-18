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
				Lijst_Namen = ["Justin", "Henk", "Jantje", "Piet", "Amelia", "Bob", "Kees", "Melle", "Sybren", "Jelly", "Nienke", "Eric", "Durk", "Jamie", "Glenn", "Corné"]

			case 8:
				print("")

			case 9:
				print("")

			case _:	print("Don't have that yet, bub")
