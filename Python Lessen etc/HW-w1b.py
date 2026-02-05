
assign = input("Which assignment do you want to see??")

try: assign = int(assign)
except ValueError: print("Das geen getal... pik")
else:
	if assign == 1:
		ans = input("Enter your name, age, and hobby, seperated by spaces!")
		anss = ans.split(" ", 2)

		try: anss[1] = int(anss[1])
		except ValueError: print("Your age wasn't a number... pik")
		else:
			print(f"\nSo your name is {anss[0]}, you're {anss[1]} years old, and like {anss[2]}??? Wow, that's crazy")
			print(f"\nIf you're {anss[1]} years old, that's about:\n\t{anss[1]*12} months or-\n\t\t{anss[1]*365} days!? WOW")

	elif assign == 2:
		a = "10"
		b = 5

		print(a + str(b)) # string:"105"
		print(int(a) + b) # int:15
		print(a * b) # string:"10 10 10 10 10"
		print(bool("")) # False, empty string
		print(bool("0")) #true, string("0") not int(0)

		# Enige wat ik even over het hoofd had gezien is gebrek aan spaties tussen de 5 * "10"

	elif assign == 3:
		print('''Q: Wat snap je nu beter dan vorige week?
	A: Ik denk niet dat er iets wat ik nu per se beter snap, alswel wat correcties op dingen die ik fout herrinderd had, zoals geen spaties bij string + string
Q: Wat vind je nog verwarrend of lastig?
	A: Ik vind heel python altijd wat verwarren tov C++ of C# bijvoorbeeld, maar tot zo ver is het zeer goed te doen voor mij. Dit is leuk, lage drempel, kennis verversen
Q: Wat viel je op aan hoe Python met types omgaat?
	A: Niks bijzonders opzich. Van wat ik mij herinner is et in principe allemaal hetzelfde als andere talen waar ik meer ervaring in heb. Het stomste aan python types vind ik het gebrek aan types declareren, lol''')
  
	else:	print("Don't have that yet, bub")
