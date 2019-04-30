from random import randint

WORD_LIST = "words.txt"
words_list=[]

with open(WORD_LIST, 'r') as wl:
    for line in wl:
        words_list.append(line)
    wl.close()

HangMan=(
"""
------
|     |
|
|
|
|
|
------------
____________
""",
"""
------
|     |
|     O
|
|
|
|
------------
____________
""",
"""
------
|     |
|   (x.x)
|     |
|
|
|
------------
____________
""",
"""
------
|     |
|     0
|    /|
|
|
|
------------
____________
""",
"""
------
|     |
|     P
|    /|\\
|
|
|
------------
____________
""",
"""
------
|     |
|     C
|    /|\\
|    /
|
|
------------
____________
""",
"""
------
|     |
|     0
|    /|\\
|    / \\
|
|
------------
____________
"""
)
class HangmanGame:

    def Get_Guess(self):
        guess = input("please input a letter between A-Z:  ")
        if not guess.isalpha() and len(guess)>1 and guess =="":
            if guess.lower() == "give up":
                self.Game_Lost()
            else:
                print("This is not a valid letter try again")
                self.Get_Guess()
        elif guess in self.Guessed_Letters:
            print("Letter was already guessed, try again")
            self.Get_Guess()
        else:
            return guess.lower()

    def Game_Running(self, tries, Failure):
        if tries == 0:
            self.Game_Lost()
        if "_" not in self.Blank_Word:
            self.Game_Win()
        print(HangMan[Failure])
        print(("\nThere are  {} letters in the secret word.").format(self.length))
        guess = self.Get_Guess()
        self.Guessed_Letters.append(guess)
        if guess not in self.secretWord:
            tries-=1
            Failure+=1
            print(("\n{} is not included in the word.").format(guess))
            self.Game_Running(tries, Failure)
        else:
            searchMore=True
            startsearchIndex= 0
            while searchMore:
                try:
                    foundAtIndex = self.secretWord.index(guess, startsearchIndex)
                    self.Blank_Word[foundAtIndex] = guess
                    startsearchIndex = foundAtIndex +1
                except:
                    searchMore=False
        print("".join(self.Blank_Word))
        self.Game_Running(tries, Failure)

    def Set_Game(self):
        self.secretWord = words_list[randint(0,20)]
        self.secretWord = self.secretWord[:-1]
        for letter in self.secretWord:
            self.Blank_Word.append("_")
        self.length=len(self.secretWord)
        print("Welcome to hangman you have 6 tries\n type give up to end it early.")
        self.Game_Running(6,0)

    def Game_Lost(self):
        print(HangMan[-1])
        print(("\nGame Over, the Word was {}\n would you like to play again?").format(self.secretWord))
        answer = input().lower()
        if answer.isalpha():
            if answer in ("yes", "y"):
                self.__init__()
                self.Set_Game()
            else:
                print("It was a pleasure. GoodBye")
                exit()
        else:
            print("Unable to tell what you want to do, so I will assume you want to quit. Good Bye!")
            exit()

    def Game_Win(self):
        print(("\nYou have won the word is {}\n would you like to play again?").format(self.secretWord))
        answer = input().lower()
        if answer.isalpha():
            if answer in ("yes", "y"):
                self.__init__()
                self.Set_Game()
            else:
                print("It was a pleasure. GoodBye")
                exit()
        else:
            print("Unable to tell what you want to do, so I will assume you want to quit. Good Bye!")
            exit()

    def __init__(self,v):
        self.Play_Again = True
        self.secretWord = ""
        self.User_Guess = ""
        self.Guessed_Letters = []
        self.Blank_Word = []
        self.length = 0
        guess= ""

def main():
    newGame = HangmanGame()
    newGame.Set_Game(10)

if __name__ == "__main__":
    main()
