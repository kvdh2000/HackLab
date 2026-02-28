''' Opdracht 3 '''
# Getal = int(input("Geef mij een getal: "))
# if Getal < 10:
#     print(f"{Getal} is kleiner dan 10")
# elif Getal == 10:
#     print(f"{Getal} is gelijk aan 10")
# else:
#     print(f"{Getal} is groter dan 10")


''' Match Case Opdracht'''
# maand = input("Van welke maand wil je het aantal dagen weten? ").capitalize()

# match maand:
#     case "Januari":
#         print("Januari heeft 31 dagen")
#     case "Februari":
#         print("Februari heeft 28 of 29 dagen")
#     case "Maart":
#         print("Maart heeft 31 dagen")
#     case "April":
#         print("April heeft 30 dagen")
#     case "Mei":
#         print("Mei heeft 31 dagen")
#     case "Juni":
#         print("Juni heeft 30 dagen")
#     case "Juli":
#         print("Juli heeft 31 dagen")
#     case "Augustus":
#         print("Augustus heeft 31 dagen")
#     case "September":
#         print("September heeft 30 dagen")
#     case "Oktober":
#         print("Oktober heeft 31 dagen")
#     case "November":
#         print("November heeft 30 dagen")
#     case "December":
#         print("December heeft 31 dagen")
#     case _:
#         print("Dat is niet een maand vriend")

# match maand:
#     case "Januari" | "Maart" | "Mei" | "Juli" | "Augustus" | "Oktober" | "December":
#         print(f"{maand} heeft 31 dagen")
#     case "April" | "Juni" | "September" | "November" :
#         print(f"{maand} heeft 30 dagen")
#     case "Februari" :
#         print("Februari heeft 28 of 29 dagen")
#     case _:
#         print("Dat is niet een maand vriend")




''' Opdracht 4 '''
# getal = int(input("Geef me een getal om te vermenigvuldigen: "))
# for i in range(1, 11, 1):
#     print(f"{i} x {getal} = {i * getal}")


''' Opdracht 5 '''
' Bodge: '
# for i in range(1, 101):
#     if i % 5 == 0 and i % 7 == 0: #Checkt of een getal deelbaar is door 3 én 5, geeft FizzBuzz terug
#         print("FizzBuzz")
#     elif i % 5 == 0: #Als een getal niet deelbaar is door 3 én 5, checkt of het getal alleen deelbaar is door 3, geeft Fizz terug
#         print("Fizz")
#     elif i % 7 == 0: #Als een getal niet deebaar is door 3 én 5, en niet door 3, checkt of het getal alleen deelbaar is door 5, geeft Buzz terug
#         print("Buzz")
#     else:
#         print(i)

' Elegant: '
# for i in range(1, 101):
#     x = ""
#     if i % 5 == 0:
#         x += "Fizz"
#     if i % 7 == 0:
#         x += "Buzz"
#     if x == "":
#         x = i
#     print(x)

' Functioneel: '
# def Fizz(n): #Checkt of n ( = i) weg te delen is door 5
#     if n % 5 == 0:
#         return "Fizz"
#     else:
#         return ""

# def Buzz(n): #Checkt of n ( = i) weg te delen is door 7
#     if n % 7 == 0:
#         return "Buzz"
#     else:
#         return ""

# for i in range(1,101):
#     x = ""
#     x += Fizz(i) #Vult x aan met Fizz als i weg te delen is door 5
#     x += Buzz(i) #Vult x aan met Buzz als i weg te delen is door 7
#     if x == "": 
#         x = i #Maakt x = i als i niet weg te delen is door 5 of 7
#     print(x)


''' Opdracht 6 '''
# bouw = "op"
# ats = ""
# arrowlen = 15
# arrowlen = int(input("Hoe groot wil je de pijl maken?\n"))

# for i in range(arrowlen):
#     if bouw == "op":
#         ats += "@"
#         print(ats)
#         if len(ats) >= arrowlen/2:
#             bouw = "af"
#     elif bouw == "af":
#         if len(ats) == 1:
#             break
#         ats = ats[:-1]
#         print(ats)

# while len(ats) <= arrowlen:
#     if bouw == "op":
#         ats += "@"
#         print(ats)
#         if len(ats) >= arrowlen/2:
#             bouw = "af"
#     elif bouw == "af":
#         if len(ats) == 1:
#             break
#         ats = ats[:-1]
#         print(ats)


''' A New DNA'''
# sequence = "CCCCAAATTTTTCAATTCTA"
# complementary = ""
# for i in sequence:
#     if i == 'A':
#         complementary += 'T'
#     elif i == 'T':
#         complementary += 'A'
#     elif i == 'C':
#         complementary += 'G'
#     elif i == 'G':
#         complementary += 'C'
#     else:
#         print("Your DNA's fucked mate")
#         complementary += '?'
# print(sequence)
# print("|"*len(sequence))
# print(complementary)


''' Opdracht 7A
Maak een variabele, Lijst_Namen, met meerdere namen
Print de namen uit Lijst_Namen allemaal met verschillende formattering in strings uit (f-string, string.format en string concatenation)
'''

''' Opdracht 7B
Print met de lijst en indexering de HELE zin "Hallo, ik ben [naam] en ik zit bij Hacklab"
Dus niet alleen je eigen naam in de zin!
Met een formattering van {letterList[25].upper()}{letterList[18]}{letterList[3]}{letterList[4]}{letterList[7]}{letterList[24]}
'''

''' Opdracht 8A
Maak een list met Verschillende dingen (bijvoorbeeld een auto merk, een vliegtuigmodel, een diersoort, een land)
Maak een lege dictionary
Vul deze dictionary met Key/Value pairs met de Dictionary['key'] = Value.
Bepaal de Values aan de hand van list Indexes
'''

''' Opdracht 8B
Zoek 'Het antwoord' in de volgende dict, en de dict keys die je nodig hebt om deze te bereiken. Voor meerdere dicts in elkaar gebruik je de formattering van ['nou nog eentje dan']['nou nog eentje dan']
Zoektocht['dict']['dict']....['dict']['Deze']
'''

Zoektocht = {'dict' : {'dict' : {'dict' : {'dict' : {'Niet deze': "Geen antwoord", 'Ook niet deze': 0, 'Nope': "Nee"}, 'list': [["bla", 15, "asdf51sf", "Hallo", ["bla", 15, "asdf51sf", "Hallo"]]], 'ding': "aaaaaaaa", 'Nog een': 15, 'nou nog eentje dan': {'Niet deze': "Geen antwoord", 'Ook niet deze': 0, 'Nope': "Nee"}}, 'list': ["bla", 15, "asdf51sf", "Hallo", ["bla", 15, "asdf51sf", "Hallo"]], 'ding': "aaaaaaaa", 'Nog een': 15, 'nou nog eentje dan': {'dict' : {'Niet deze': "Geen antwoord", 'Ook niet deze': 0, 'Nope': "Nee"}, 'list': [["bla", 15, "asdf51sf", "Hallo", ["bla", 15, "asdf51sf", "Hallo"]]], 'ding': "aaaaaaaa", 'Nog een': 15, 'nou nog eentje dan': {'Niet deze': "Geen antwoord", 'Ook niet deze': 0, 'Nope': "Nee"}}}, 'list': [["bla", 15, "asdf51sf", "Hallo", ["bla", 15, "asdf51sf", "Hallo"]]], 'ding': "aaaaaaaa", 'Nog een': 15, 'nou nog eentje dan': {'dict' : {'dict' : {'Niet deze': "Geen antwoord", 'Ook niet deze': 0, 'Nope': "Nee"}, 'list': [["bla", 15, "asdf51sf", "Hallo", ["bla", 15, "asdf51sf", "Hallo"]]], 'ding': "aaaaaaaa", 'Nog een': 15, 'nou nog eentje dan': {'Niet deze': "Geen antwoord", 'Ook niet deze': 0, 'Nope': "Nee"}}, 'list': ["bla", 15, "asdf51sf", "Hallo", ["bla", 15, "asdf51sf", "Hallo"]], 'ding': "aaaaaaaa", 'Nog een': 15, 'nou nog eentje dan': {'dict' : {'Niet deze': "Geen antwoord", 'Ook niet deze': 0, 'Nope': "Nee"}, 'list': [["bla", 15, "asdf51sf", "Hallo", ["bla", 15, "asdf51sf", "Hallo"]]], 'ding': "aaaaaaaa", 'Nog een': 15, 'nou nog eentje dan': {'dict' : {'dict' : {'Deze': "Het antwoord", 'Niet deze': "Geen antwoord", 'Ook niet deze': 0, 'Nope': "Nee"}, 'list': [["bla", 15, "asdf51sf", "Hallo", ["bla", 15, "asdf51sf", "Hallo"]]], 'ding': "aaaaaaaa", 'Nog een': 15, 'nou nog eentje dan': {'Niet deze': "Geen antwoord", 'Ook niet deze': 0, 'Nope': "Nee"}}, 'list': ["bla", 15, "asdf51sf", "Hallo", ["bla", 15, "asdf51sf", "Hallo"]], 'ding': "aaaaaaaa", 'Nog een': 15, 'nou nog eentje dan': {'dict' : {'Deze': "Het andwo0rdt", 'Niet deze': "Geen antwoord", 'Ook niet deze': 0, 'Nope': "Nee"}, 'list': [["bla", 15, "asdf51sf", "Hallo", ["bla", 15, "asdf51sf", "Hallo"]]], 'ding': "aaaaaaaa", 'Nog een': 15, 'nou nog eentje dan': {'Deze': "Het andw00rd", 'Niet deze': "Geen antwoord", 'Ook niet deze': 0, 'Nope': "Nee"}}}}}}, 'list': ["bla", 15, "asdf51sf", "Hallo", ["bla", 15, "asdf51sf", "Hallo"]], 'ding': "aaaaaaaa", 'Nog een': 15, 'nou nog eentje dan': {'dict' : {'Niet deze': "Geen antwoord", 'Ook niet deze': 0, 'Nope': "Nee"}, 'list': [["bla", 15, "asdf51sf", "Hallo", ["bla", 15, "asdf51sf", "Hallo"]]], 'ding': "aaaaaaaa", 'Nog een': 15, 'nou nog eentje dan': {'Deze': "Het andwoord", 'Niet deze': "Geen antwoord", 'Ook niet deze': 0, 'Nope': "Nee"}}}

'''DNA Strikes Back
Maak met behulp van een dictionary en List Comprehension code die het DNA uit de vorige les omzet naar de complementaire sequentie
'''
