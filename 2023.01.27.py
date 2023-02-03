import random
from colorama import Fore, Back, Style

words=["viens", "divi", "trīs", "cits"]

while True:
    totalLives=5
    word= random.choice(words)
    guessedWord = list("_" for _ in word)
    print(word)

    while (totalLives > 0 and not "".join(guessedWord) == word):
        inp= input("Ievade (vārds): ")
        if (len(inp) != len(word)): continue
        #inp = inp[0]
        
        guessedWord = list("_" for _ in word)
        for aaa in range(0, len(guessedWord)):
            if word[aaa]== inp[aaa]:
                guessedWord[aaa]=inp[aaa]
                print(f"{Fore.GREEN}{inp[aaa]}{Style.RESET_ALL}", end="")
            elif inp[aaa] in word:
                print (f"{Fore.YWLLOW}{inp[aaa]}{Style.RESET_ALL}", end="")
            else:
                print (f"{inp[aaa]}", end="")
        print("")
        totalLives -= 1

        #print(didGuessLetter)
        #print("".join(guessedWord))

    if (totalLives > 0): 
        print("Uzvara!")
    else:
        print("Jūs Zaudējāt!")
    if input("Vai beigt spēli vai nē? (Y/N)")[0].lower() == "y":
        break

