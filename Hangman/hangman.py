# Write your code here
import random
from string import ascii_lowercase

word = random.choice(['python', 'java', 'kotlin', 'javascript'])  # 'python', 'java', 'kotlin', 'javascript'
show_word = list('-' * (len(word)))
tried_letter = list()
counter = 1
print('H A N G M A N')

while counter <= 8 and word != ''.join(show_word):
    print()
    print(''.join(show_word))
    guess_letter = input(f'Input a letter: ')

    if len(guess_letter) < 1 or len(guess_letter) > 1:
        print('You should print a single letter')
    elif guess_letter not in ascii_lowercase:
        print('It is not an ASCII lowercase letter')
    elif guess_letter in tried_letter:
        print('You already typed this letter')
        tried_letter += guess_letter
    elif guess_letter not in word:
        print('No such letter in the word')
        counter += 1
        tried_letter += guess_letter
    if (guess_letter in word) and (guess_letter in ascii_lowercase) and (len(guess_letter) == 1):
        for p in range(len(word)):
            if guess_letter == word[p]:
                show_word[p] = word[p]
        tried_letter += guess_letter
if ''.join(show_word) == word:
    print(f'You guessed the {word}!')
    print('You survived!')
else:
    print('You are hanged!')
