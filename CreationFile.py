import random
import re

class Complete_Word:
    def __init__(self,wordlist):
        self.wordlist=wordlist
        self.attempts_remain=6
        self.current_letter = ''
        self.chosen_word = ''
        self.guessed_letter = []

    def choose_the_word(self):
        file = open(self.wordlist)
        words = file.read().split('\n')
        word_count = len(words)
        self.chosen_word = words[random.randrange(0,word_count)]
        self.word_status = ['-' for i in range(len(self.chosen_word))]

    def fill_the_word_status(self):
        nos = random.randrange(1,3)   #How many letters should be visible in letter
        for i in range(nos):
            position =random.randrange(0,len(self.chosen_word))
            self.word_status[position] = self.chosen_word[position]

    def guess_the_letter(self):
        letter = input("Guess the letter: ")

        if(letter in self.guessed_letter):
            print("You have already guessed this...! Your guesses {}", format(self.guessed_letter))
            return letter
        self.guessed_letter.append(letter)
        occurences = []
        occurence = re.finditer(letter,self.chosen_word)

        for m in occurence:
            occurences.append(m.start())

        if(len(occurences) == 0):
                self.attempts_remain -=1
                print("Sorry!! wrong letter chose... Attempts remaining->",self.attempts_remain)
        else:
            for pos in occurences:

                self.word_status[pos] = self.chosen_word[pos]
                print("Correct Choise!!!")

    def get_word_status(self):
        print("Current Word Status: {}\n".format(''.join(self.word_status)))



