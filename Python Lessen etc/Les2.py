''' If statements '''

# print("a" == "b")
# print("a" != "b")
# print(1 <= 1)
# print(1 >= 2)
# print(1.0 == 1)
# a = 5
# b = 5
# print(a == b)

# if [vergelijking]:
#     [uit te voeren code]


# if 1 == 1:
#     print("Hello World")
#     print("Hallo Klas")
#     if 2 == 2:
#         print("We gaan dieper")

# if 1 != 1:
#     print("Hello World")
#     print("Hallo Klas")

# a = 0
# if a:
#     print("Hallo klas")

# Zin = "Hallo wereld, klas en Justin"
# if "Justin" in Zin:
#     print("Zo dus")

# if "a" == "b" or 1 == 1:
#     print("Hello World")
#     print("Hallo Klas")

# if "a" == "b" or 1 == 2:
#     print("Hello World")
#     print("Hallo Klas")

# if "a" == "a" and 1 == 1:
#     print("Hello World")
#     print("Hallo Klas")

# if "a" == "a" and 1 == 2:
#     print("Hello World")
#     print("Hallo Klas")    

getal = 5

# if getal == 6:
#     print("Hello World")
#     print("Hallo Klas")  

# if "a" == "a" and "b" == "b" or "1" == 1 and 1 == "1":
#     print("Whaddup")

# print(("a" == "a") and ("b" == "b"))
# print(("1" == 1) and (1 == "1"))
# print((("a" == "a") and ("b" == "b")) or (("1" == 1) and (1 == "1")))


# if [vergelijking]:
#     [uit te voeren code]
# else:
#     [uit te voeren code]

# Naam = input("Wat is je naam? ").capitalize()
# if Naam == "Martin" or Naam == "Glenn" or Naam == "Melle" or Naam == "Justin":
#     print("Hallo Leraar")
# else:
#     print("Hallo Leerling")

# if [vergelijking]:
#     [uit te voeren code]
# elif [andere vergelijking]:
#     [andere uit te voeren code]
# else:
#     [uit te voeren code]

# Dag = input("Welke dag is het vandaag? ").capitalize()
# if Dag == "Maandag" or Dag == "Dinsdag" or Dag == "Woensdag":
#     print("Nog lang geen weekend :(")
# elif Dag == "Donderdag" or Dag == "Vrijdag":
#     print("Bijna weekend :)")
# elif Dag == "Zaterdag" or Dag == "Zondag":
#     print("Weekend :D")
# else:
#     print("Kunde wel spellen?!")



''' Switch Cases'''


# match [variabele]
#     case [mogelijke inhoud variabele]:
#         [uit te voeren code]
#     case [mogelijke inhoud variabele]:
#         [uit te voeren code]
#     case _:
#         [alternatief uit te voeren code]

# dag = input("Welke dag is het vandaag? ").capitalize()

# match dag:
#     case "Maandag":
#         print("Een nieuwe week vol mogelijkheden!")
#     case "Dinsdag":
#         print("Ok de week is nu echt begonnen")
#     case "Woensdag":
#         print("We zijn al op de helft!")
#     case "Donderdag":
#         print("Bijna weekend, maar wel de langste werkdag")
#     case "Vrijdag":
#         print("Laatste dagje, vandaag visdag?")
#     case "Zaterdag":
#         print("Eindelijk weekend, wel nog even boodschappen doen")
#     case "Zondag":
#         print("Laatste dagje weekend al weer, tijd om schoon te maken")
#     case _:
#         print("Da's geen dag van de week, pik")

# match dag:
#     case "Maandag" | "Dinsdag" | "Woensdag":
#         print("Nog lang geen weekend :(")
#     case "Donderdag" | "Vrijdag":
#         print("Bijna weekend :)")
#     case "Zaterdag" | "Zondag":
#         print("Weekend :D")
#     case _:
#         print("Kunde wel spellen?!")

getal1 = 20
getal2 = 30

# if getal1 > getal2:
#     print(f"Getal 1 ({getal1}) > Getal 2 ({getal2})")
# elif getal1 < getal2:
#     print(f"Getal 1 ({getal1}) < Getal 2 ({getal2})") 
# else:
#     print("The numbers don't math right, somehow")

# match getal1 > getal2:
#     case False:
#         print(f"Getal 1 ({getal1}) < Getal 2 ({getal2})")
#     case True:
#         print(f"Getal 1 ({getal1}) > Getal 2 ({getal2})")
#     case _:
#         print("The numbers don't math right, somehow")



''' For Loops '''

zin = "Hallo allemaal, dit is een voorbeeld voor For Loops!"
nummer = 16584651

# for [variable] in [iterable]:
#     [uit te voeren code]


# for letter in zin:
#     print(letter)
#     zin += letter
# print(zin)

# for getal in nummer:
#     print(getal)

# range(start, stop, step)

# a = range(5)
# print(type(a))
# print(a)
# print(range(10))
# print(range(10, 20))
# print(range(10, 100, 10))

# print(range(0, 11, 1))
# for i in range(0, 11, 1):
# for i in range(11):
#     print(i)

# for i in range(0, 10, 1):
#     print(i)

# for i in range(10, -1, -1):
#     print(i)


''' While Loops '''
# i = 0
# while i <= 100:
#     print(i)
#     i += 1

from time import sleep

# i = 0
# while True:
#     print(i)
#     i += 1
#     sleep(.1)
#     if i > 100:
#         break
# print("Hallo mensen")

i = 1
while i <= 100:
    if i % 3 == 0:
        print(f"{i} is wegdeelbaar door 3")
        i += 1
    else:
        print(i)
        i += 1


''' Logica Puzzels:
https://www.youtube.com/watch?v=7yDmGnA8Hw0
https://www.youtube.com/watch?v=9uZ-jeZS8d0
https://www.youtube.com/watch?v=N5vJSNXPEwA
https://www.youtube.com/watch?v=rn1mjuVXNEI
'''