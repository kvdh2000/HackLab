# def Codon_Translate(Codons, sequence):
#     First, Second, Third = 0, 1, 2
#     Codon_List = []
#     while First <= len(sequence)-1 and Second <= len(sequence)-1 and Third <= len(sequence)-1:
#         Codon_List.append(Codons[sequence[First]][sequence[Second]][sequence[Third]])
#         First += 3
#         Second += 3
#         Third += 3
#     Last_nucs = len(sequence) % 3
#     if Last_nucs == 1:
#         Codon_List.append(Codons[sequence[-1]])
#     elif Last_nucs == 2:
#         Codon_List.append(Codons[sequence[-2]][sequence[-1]])
#     return Codon_List

# def Codon_Translate_2(Codons, sequence):
#     Codon_List = []
#     remains = len(sequence) % 3
#     for i in range(0, len(sequence) - remains, 3):
#     # for i in range(0, len(sequence), 3):
#         Codon_List.append(Codons[sequence[i]][sequence[i+1]][sequence[i+2]])
#     if remains == 1:
#         Codon_Set = set()
#         for nuc in Codons[sequence[-1]]:
#             for nucnuc in Codons[sequence[-1]]:
#                 Codon_Set.add(Codons[sequence[-1]][nuc][nucnuc])
#         Codon_List.append(list(Codon_Set))
#     elif remains == 2:
#         Codon_List.append(list(set(Codons[sequence[-2]][sequence[-1]].values())))
#     return Codon_List

# Codon_Dict = {'T' : {'T' : {'T' : "Phenylalanine", 'C' : "Phenylalanine", 'A' : "Leucine", 'G' : "Leucine"},'C' : {'T' : "Serine", 'C' : "Serine", 'A' : "Serine", 'G' : "Serine"}, 'A' : {'T' : "Tyrosine", 'C' : "Tyrosine", 'A' : "Stop (Ochre)", 'G' : "Stop (Amber)"}, 'G' : {'T' : "Cysteine", 'C' : "Cysteine", 'A' : "Stop (Opal)", 'G' : "Tryptophan"}}, 'C' : {'T' : {'T' : "Leucine", 'C' : "Leucine", 'A' : "Leucine", 'G' : "Leucine"}, 'C' : {'T' : "Proline", 'C' : "Proline", 'A' : "Proline", 'G' : "Proline"}, 'A' : {'T' : "Histidine", 'C' : "Histidine", 'A' : "Glutamine", 'G' : "Glutamine"}, 'G' : {'T' : "Arginine", 'C' : "Arginine", 'A' : "Arginine", 'G' : "Arginine"}}, 'A' : {'T' : { 'T' : "Isoleucine", 'C' : "Isoleucine", 'A' : "Isoleucine", 'G' : "Methionine"}, 'C' : {'T' : "Threonine", 'C' : "Threonine", 'A' : "Threonine", 'G' : "Threonine"}, 'A' : {'T' : "Asparagine", 'C' : "Asparagine", 'A' : "Lysine", 'G' : "Lysine"}, 'G' : {'T' : "Serine", 'C' : "Serine", 'A' : "Arginine", 'G' : "Arginine"}}, 'G' : {'T' : { 'T' : "Valine", 'C' : "Valine", 'A' : "Valine", 'G' : "Valine"}, 'C' : {'T' : "Alanine", 'C' : "Alanine", 'A' : "Alanine", 'G' : "Alanine"}, 'A' : {'T' : "Aspartic acid", 'C' : "Aspartic acid", 'A' : "Glutamic acid", 'G' : "Glutamic acid"}, 'G' : {'T' : "Glycine", 'C' : "Glycine", 'A' : "Glycine", 'G' : "Glycine"}}}

# from DNA_Generator import DNA_Gen

# DNA_seq = DNA_Gen(20)
# DNA_seq = "CAAGGCCTGAATCCCAATAT"
# print(DNA_seq)
# print(DNA_seq[:-1])

# print(Codon_Translate(Codon_Dict, DNA_seq))
# print(Codon_Translate(Codon_Dict, DNA_seq[:-1]))

# print(Codon_Translate_2(Codon_Dict, DNA_seq))
# print(Codon_Translate_2(Codon_Dict, DNA_seq[:-1]))



''' Opdracht 9'''
# def XO(string):
#     x = 0
#     o = 0
#     for i in string:
#         if i == "x" or i == "X":
#             x += 1
#         elif i == "o" or i == "O":
#             o += 1
#     return x == o

# def XO(string):
#     return string.upper().count("X") == string.upper().count("O")

# print(XO("ooxx")) # True
# print(XO("xooxx")) # False
# print(XO("ooxXm")) # True
# print(XO("zpzpzpp")) # True
# print(XO("zzoo")) # False


''' Opdracht 10 '''
# def hamming_distance(string1, string2):
#     if len(string1) != len(string2):
#         return "String lengths don't match!"
#     ham_dist = 0
#     for i in range(len(string1)):
#         if string1[i] != string2[i]:
#             ham_dist += 1
#     return ham_dist

# def hamming_distance(string1, string2):
#     return len([1 for i in range(len(string1)) if string1[i] != string2[i]])

# print(hamming_distance("abcde", "bcdef")) # 5
# print(hamming_distance("abcde", "abcde")) # 0
# print(hamming_distance("strong", "strung")) # 1


''' Opdracht 11 '''
# def list_op(x, y, n):
#     lst = []
#     for i in range(x, y+1):
#         if i % n == 0:
#             lst.append(i)
#     return lst

# def list_op(x, y, n):
#     return [i for i in range(x, y+1) if i % n == 0]

# print(list_op(1, 10, 3)) # [3, 6, 9]
# print(list_op(7, 9, 2)) # [8]
# print(list_op(15, 20, 7)) # []




''' Opdracht 12 '''
# def double_letters(string):
#     new_string = ""
#     for i in string:
#         new_string += 2 * i
#     return new_string

# def double_letters(string):
#     return "".join([let*2 for let in string])

# print(double_letters("String"))
# print(double_letters("Hello World!"))
# print(double_letters("1234!_ "))

''' Opdracht 13 (Return of the DNA)
Eigen Functie schrijven om DNA van [x] lengte te genereren, en met behulp van een 2e functie een complementaire sequence te genereren
'''

''' Opdracht 14
Schrijf een functie die een muntje [x] maal opgooit en de aantal keer kop en munt teruggeeft
'''


''' Opdracht 15
https://edabit.com/challenge/9hQogtkbZSSJ8tYsG
'''


''' Opdracht 16
https://edabit.com/challenge/eJLwXpuaffjFnzENN
'''


''' Opdracht 17
https://edabit.com/challenge/KEz3TAQfh9WxSZMLH
'''


''' Opdracht 18
https://edabit.com/challenge/nFA52oAmxjebgpPQy
'''

''' Opdracht 19
Extra gelegenheid om je galgje spel te verbeteren of af te maken. Dit werkt 
werkt in je voordeel als er twijfel is of je door kan stromen.
'''