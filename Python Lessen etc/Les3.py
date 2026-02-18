''' Lists '''

# var_name = [entry1, entry2, entry3]
Lijst_Namen_1 = ["Justin", "Henk", "Jantje", "Piet", "Amelia", "Bob", "Kees", "Melle", "Sybren", "Jelly", "Nienke", "Eric", "Durk", "Jamie", "Glenn", "Corné"]
rand_list = ["Naam", 5, 5.1, True, ["Justin", "Henk", "Jantje", "Piet", "Amelia", "Bob", "Kees", "Melle", "Sybren", "Jelly", "Nienke", "Eric", "Durk", "Jamie", "Glenn", "Corné"]]
Naam = "Justin"
Lijst_Nummers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 7, 4, 2, 9, 10]

# print(Lijst_Namen_1[0])

# print(Lijst_Namen_1[-1])
# print(Naam[5])
# print(rand_list[4][7])
# print(Lijst_Namen_1[-1][-1])
# print(len(Lijst_Namen_1))
# print(len(rand_list))
# print(len(rand_list[4]))
# print(Lijst_Namen_1[len(Lijst_Namen_1) - 1])
# print(rand_list[4][0])
# print(Lijst_Namen_1[20])

# Lijst_Namen_1[0] += " Bötger"
# print(Lijst_Namen_1[0])

Lijst_Namen_2 = Lijst_Namen_1.copy()
Lijst_Namen_3 = Lijst_Namen_1

# print(Lijst_Namen_1)
# print(Lijst_Namen_2)
# print(Lijst_Namen_3)

# print (Lijst_Namen_1 == Lijst_Namen_3)
# print(Lijst_Namen_1 == Lijst_Namen_2)

# Lijst_Namen_3[0] = "Bob"
# print(Lijst_Namen_1)
# print(Lijst_Namen_2)
# print(Lijst_Namen_3)

# print(id(Lijst_Namen_1))
# print(id(Lijst_Namen_2))
# print(id(Lijst_Namen_3))

# print(id(Lijst_Namen_1) == id(Lijst_Namen_3))
# print(id(Lijst_Namen_1) == id(Lijst_Namen_2))


# Lijst_Namen_2[0] = "Bob"
# print(Lijst_Namen_1)
# print(Lijst_Namen_2)
# print(Lijst_Namen_3)


Super_Lijst_Namen = Lijst_Namen_1 + Lijst_Namen_3

# print(Super_Lijst_Namen)
# print(len(Super_Lijst_Namen))
# while "Justin" in Super_Lijst_Namen:
#     Super_Lijst_Namen.remove("Justin")
# print(Super_Lijst_Namen)
# print(len(Super_Lijst_Namen))

# rand_list[4].remove("Justin")
# print(rand_list)

Turbo_Lijst_Namen = Lijst_Namen_1 * 3
# print(Turbo_Lijst_Namen)

# for i in range(len(Super_Lijst_Namen)):
#     print(i)
#     if Super_Lijst_Namen[i] == "Justin":
#         print(Super_Lijst_Namen.pop(i))
#         i -= 1
# print(Super_Lijst_Namen)
# x = 0
# for naam in Super_Lijst_Namen:
#     print(naam)
#     x += 1
#     if naam == "Justin":
#         Super_Lijst_Namen.remove("Justin")
# print(x)

# print(len(Super_Lijst_Namen))
# print(Super_Lijst_Namen.pop(5))
# print(len(Super_Lijst_Namen))

# print(Lijst_Namen_1)
# print(len(Lijst_Namen_1))
# Lijst_Namen_1.remove("Bob")
# print(len(Lijst_Namen_1))
# print(Lijst_Namen_1)

# print(len(Lijst_Namen_1))
# Lijst_Namen_1.remove(Lijst_Namen_1[3])
# print(len(Lijst_Namen_1))
# print(Lijst_Namen_1)

# print(Lijst_Namen_1)
# Lijst_Namen_1.append("Bob")
# Lijst_Namen_1.insert(4, "Karel")
# print(Lijst_Namen_1)



voorbeeld = "HalloHallo"
# print(voorbeeld[5])

# print(Lijst_Namen_1)
# del(Lijst_Namen_1[1])
# print(Lijst_Namen_1)

# print(voorbeeld)
# del(voorbeeld[5])
# print(voorbeeld)

# print(Lijst_Namen_1)
# print(Lijst_Nummers)
# Lijst_Namen_1.sort()
# Lijst_Nummers.sort()
# print(Lijst_Namen_1)
# print(Lijst_Nummers)

# Lijst_Nummers.append(5.6)

# Lijst_Nummers_Namen = Lijst_Nummers + Lijst_Namen_1
# Lijst_Nummers_Namen.sort()
# print(Lijst_Nummers_Namen)
# Lijst_Nummers.sort()
# print(Lijst_Nummers)

Lijst_Namen_4 = ["Justin", "Amir", "Timiro", "Valentijn", "Pieter", "Vinay", "Johan", "Rosalijn", "Jildau", "Raimond", "Albert", "Kees", "Dennis", "Ruben", "Lutsen", "Jari", ["Justin", "Amir", "Timiro", "Valentijn", "Pieter", "Vinay", "Johan", "Rosalijn", "Jildau", "Raimond", "Albert", "Kees", "Dennis", "Ruben", "Lutsen", "Jari"]]

# for naam in Lijst_Namen_4:
#     print(naam)
#     if type(naam) == list:
#         print(Lijst_Namen_4.index(naam))
#         print(naam.index("Justin"))

# print(Lijst_Namen_4.index("Justin"))
# print(Lijst_Namen_4[2])
# print(Lijst_Namen_4[5])
# print(Lijst_Namen_4[5][3])

# if "Justin" in Lijst_Namen_1:
#     print("Hallo Justin")

# print(Super_Lijst_Namen)
# print(Super_Lijst_Namen[2:])
# print(Super_Lijst_Namen[:6])

''' List Comprehension '''

# Numlist = []
# for i in range(101):
#     if i % 5 == 0 or i % 7 == 0:
#         Numlist.append(i)
# print(Numlist)

# fizzbuzzlist2 = [i for i in range(101) if ((i % 5 == 0) or (i % 7 == 0))]
# Niew_Namenlijst = [Naam for Naam in Lijst_Namen_1 if Naam == "Justin"]
# print(Niew_Namenlijst)

# print(fizzbuzzlist2)


''' Dictionaries '''
Dictionary = {"Key" : "Waarde", "Key2" : "Waarde2"}


# Dict_Dingen = {"Dier" : "Hond", "Voertuig" : "Auto", "Weer" : "Zon", "Temperatuur" : f"{20} graden", "Getal" : 5, 2 : "Twee"}
# print(Dict_Dingen)

# Dict_Dingen = {"Dier":"Hond", "Voertuig":"Auto", "Weer":"Zon", "Temperatuur": "20 graden", "Getal": 5, "Getal" : 10}
# print(Dict_Dingen)

Dict_Dingen = {"Dier":"Hond", "Voertuig":"Auto", "Weer":"Zon", "Temperatuur" :f"{20} graden", "Lijst" : [1, 2, 3, 4]}

# print(Dict_Dingen)
# print(Dict_Dingen['Dier'])
# print(Dict_Dingen['Lijst'][2])

# tuple_list = Dict_Dingen.items()
# tuple_list = list(Dict_Dingen.items())
# print(tuple_list)
# print(tuple_list[1])

Dict_Dingen = {"Dier":"Hond", "Voertuig":"Auto", "Weer":"Zon", "Temperatuur":f"{20} graden", "Getal": 5}

# print(Dict_Dingen.keys())

# if 'Dier' in Dict_Dingen:
#     print(Dict_Dingen['Dier'])

# for i in Dict_Dingen:
#     print(i)

# for i in Dict_Dingen:
#     print(Dict_Dingen[i])

Key = "Drinken"
Waarde = "Bier"

# Dict_Dingen[Key] = Waarde
# Dict_Dingen['Naam'] = "Bob"
# Dict_Dingen['Les'] = "Vandaag"
# Dict_Dingen['Dier'] = "Kat"
# print(Dict_Dingen['Les'])
# print(Dict_Dingen)

# print(Dict_Dingen)
# print(Dict_Dingen.pop('Voertuig'))
# print(Dict_Dingen)

# del Dict_Dingen['Voertuig']
# print(Dict_Dingen)

# Dier = Dict_Dingen['Dier']
# print(Dier)


# print(f"Het dier is een {Dict_Dingen["Dier"]}")

# Dict_Dingen['Dier'] += "Kat"
# print(Dict_Dingen['Dier'])
# Dict_Dingen['Dier'] = Dict_Dingen['Dier'] + "Kat"
# # print(Dict_Dingen['Dier'])
# Dict_Dingen['Getal'] *= 5
# print(Dict_Dingen['Getal'])

# print(Dict_Dingen)


Dict_Dingen = {"Dier":"Hond", "Voertuig":"Auto", "Weer":"Zon", "Temperatuur":f"{20} graden", "Getal": 5, 'Numlist' : [0, 1, 2, 3, 4, 5, 6, 7, 8, 7, 4, 2, 9, 10]}
# print(Dict_Dingen['Numlist'][13])