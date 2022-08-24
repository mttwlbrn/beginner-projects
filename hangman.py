import random
from re import A
from words import words
import string

def get_valid_word(words):
    word = random.choice(words) #randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #what the user has guessed

    lives = 6

    # getting user input
    while len(word_letters) > 0 and lives > 0: 
        #letters used
        #' '.join(['a', 'b', 'cd']) --> ' a b cd'
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        #what current wors is (W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                
            else: 
                lives = lives - 1 #takes away a life if wrong
                print('Letter is not in word.')

        elif user_letter in used_letters:
            print('You already guessed that letter. Please try again.')
        
        else:
            print('Invalid character.')

    #gets here when len(word_letters) == 0 OR when lives == 0 
    #print('You got the correct word: ', ' '.join(word_list))
    if lives == 0:
        print('You died! The word was', word)
    else:
        print('You have guessed the word', word,'!!')

#user_input = input('Type something: ')
#print(user_input)

hangman()