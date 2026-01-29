
assign = input("Which assignment do you want to see??")

try: assign = int(assign)
except ValueError: print("Das geen getal... pik")
else:
	if assign == 1:
		''' Opdracht 1
		Tijd omrekenen
		Maak een variabele aan voor aantal uren
		Uur naar minuten
		Minuten naar Seconden
		Print deze getallen leuk uit
		'''

		hours = input("Enter a number of hours:")

		try: hours = int(hours)
		except ValueError: print("Das geen getal... pik")
		else: print("You imput {} hours; which is {} minutes, or {} seconds".format(hours, hours*60, hours*60*60))
	
	elif assign == 2:
		''' Opdracht 2
		Automatisch Tafel Berekenen (e.g. 1 * x, 2 * x, etc t/m 10 * x)
		Input voor welke tafel
		Print statements voor elke berekening, en toon de berekening zelf ook
		Gebruik GEEN for of while, of andere loop, maar aparte regels
		Of anders.
		'''

		num = input("Input a table to multiply:")

		try: num = int(num)			
		except ValueError: print("Das geen getal... pik")
		else: 
			table = num

			print(num)
			num+=table
			print(num)
			num+=table
			print(num)
			num+=table
			print(num)
			num+=table
			print(num)
			num+=table
			print(num)
			num+=table
			print(num)
			num+=table
			print(num)
			num+=table
			print(num)
			num+=table
			print(num)
   
			# en met een for loopje, omdat het kan
			# for i in range (0, 10):
			# 	print (num)
			# 	num+=table
	
	else:	print("Don't have that yet, bub")
