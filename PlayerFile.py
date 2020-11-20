import CreationFile

Complete_Word = CreationFile.Complete_Word('wordlist.txt')
Complete_Word.choose_the_word()
Complete_Word.fill_the_word_status()

while True:
    Complete_Word.get_word_status()
    Complete_Word.guess_the_letter()

    if(Complete_Word.attempts_remain == 0):
        print("Oops!!!... No Attempts remaining.!!.. Game Over!!!..\n The actual word was {}",format(hangman.chosen_word))
        break
    elif(Complete_Word.chosen_word == (''.join(Complete_Word.word_status))):
        Complete_Word.get_word_status()
        print("Congratulations...!!! The word is completed...!!")
        break
