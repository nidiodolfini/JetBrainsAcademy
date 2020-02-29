# Write your code here
import random
from string import ascii_lowercase

word = random.choice(['python', 'java', 'kotlin', 'javascript'])
hidden_word = '-' * (len(word))
show_word = list(hidden_word)
tried_letter = list()
counter = 0
print('H A N G M A N')

while counter < 8 and word != ''.join(show_word):
    print()
    print(''.join(show_word))
    guess_letter = input(f'Input a letter: ')
    if (guess_letter in word) and (guess_letter in ascii_lowercase) and (len(guess_letter) == 1):
        if guess_letter in show_word:
            print('You already typed this letter')
        else:
            for p in range(len(word)):
                if guess_letter == word[p]:
                    show_word[p] = guess_letter
    elif len(guess_letter) < 1 or len(guess_letter) > 1:
        print('You should print a single letter')
    elif (guess_letter not in ascii_lowercase) and (len(guess_letter) == 1):
        print('It is not an ASCII lowercase letter')
    elif guess_letter in tried_letter:
        print('You already typed this letter')
    else:
        print('No such letter in the word')
        counter += 1
    tried_letter += guess_letter
if ''.join(show_word) == word:
    print(f'You guessed the {word}!')
    print('You survived!')
else:
    print('You are hanged!')
