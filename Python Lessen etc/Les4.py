''' Functies '''
# def [naam](arguments):
#     [Uit te voeren code]


# def greeting():
#     print("Hallo Justin!")

# greeting()


def greeting(Name):
    print(f"Hello {Name}!")

# greeting("Bob")
# greeting("Henk")
# greeting()

# greeting(input("Wat is je naam?" ))

# def rekensom():
#     getal1 = int(input("Geef een getal: "))
#     getal2 = int(input("Geef een tweede getal: "))
#     print(getal1 * getal2)

# rekensom()

# def greeting(Name, Job):
#     print(f"Hallo {Name}, hoe is het als {Job}?")

# greeting("Justin", "Leraar")

# def greeting(Name, Age):
#     print(f"Hallo {Name}, je bent {Age} jaar oud")
#     print("Hallo " + Name + ", je bent " + str(Age) + " jaar oud")

# greeting("Justin", 31)

# def rekenen(getal):
#     cijfer = 10
#     resultaat = getal * cijfer
#     return resultaat

# som = rekenen(5)
# print(som)

# print(rekenen(5))

# som = rekenen(som)
# print(som)


# def recursie(getal):
#     if getal == 1:
#         return getal
#     else:
#         return recursie(getal-1)

# def recursie(getal):

#     resultaat = getal * 10
#     if resultaat % 4 == 0:
#         return resultaat
#     else:
#         return recursie(resultaat)

# print(recursie(4))
# print(recursie(-999))
# print(recursie(-1000))
# https://giphy.com/gifs/homer-simpson-the-simpsons-3ov9jQX2Ow4bM5xxuM



# def functie_1():
#     functie_2()


# def functie_2():
#     print("Allo allo")

# functie_1()


# def grote_som(argument1 = 1, argument2 = 2, argument3 = 3):
#     print(argument1)
#     print(argument2)
#     print(argument3)
#     return argument1 * argument2 * argument3

# def grote_som(argument1, argument2, argument3):
#     print(argument1)
#     print(argument2)
#     print(argument3)
#     return argument1 * argument2 * argument3

# print(grote_som(5, 5))

# getal_1 = 4
# getal_2 = 5
# getal_3 = 6

# print(grote_som(getal_1, getal_3))


# Python doet niet aan functie overloaden!

# def rekenen(getal1, getal2):
#     return getal1 * getal2

# def rekenen(getal):
#     return 5 * getal


# som = rekenen(5)
# print(som)
# print(rekenen(5))
# som = rekenen(5, 10)
# print(som)

# def ding():
#     print(blarp)

# def ding(text):
#     print(text)

# blarp = "aaaaa"
# kaas = "aapjes"
# ding(blarp)
# ding(5)
# print(kaas)

# ding()

def turbosom(Getal1, Getal2):
    '''
    Doet een machtsberekening van de twee aangeleverde getallen

    Args:
        Getal1: Getal wat tot de macht van het tweede getal wordt verheft
        Getal2: Getal wat voor de machtsverheffing wordt gebruikt

    Return:
        Een machtsverheffing van de twee getallen
    '''
    return Getal1 ** Getal2

print(turbosom(4, 2))


''' Galgje
Met functies besproken hebben jullie alle handvaten om zelf galgje te programmeren! Met nog een extra stukje code van mij om een woordlijst te maken en er een woord uit te kiezen, kunnen jullie los gaan! Tussendoor vragen//feedback mag altijd!
'''

import random

def wordchoice():
    """ 
    Maakt een list van woorden uit Woordlijst.txt, en geeft er daar een van terug

    Returns: 
        Een woord, in string vorm
    
    """
    wordlist = []
    filepath = "Woordlijst.txt"
    with open(filepath, "r") as words:
    #Loopt door alle regels in de woordenlijst https://stackoverflow.com/questions/1323364/in-python-how-to-check-if-a-string-only-contains-certain-characters
        for line in words:
            wordlist.append(line.strip())
    return random.choice(wordlist)

# print(wordchoice())


