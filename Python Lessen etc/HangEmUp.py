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

print(wordchoice())
