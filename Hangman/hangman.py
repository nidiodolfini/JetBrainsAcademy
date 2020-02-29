# Write your code here
import random

word = random.choice(['python', 'java', 'kotlin', 'javascript'])
hidden_word = '-' * (len(word))
show_word = list(hidden_word)
counter = 0
print('H A N G M A N')
print()
while counter < 8 and word != ''.join(show_word):
    print(''.join(show_word))
    guess_letter = input(f'Input a letter: ')
    if guess_letter in word:
        if guess_letter in show_word:
            print('No improvements')
            counter += 1
            if counter < 8:
                print()
        else:
            for p in range(len(word)):
                if guess_letter == word[p]:
                    show_word[p] = guess_letter
            if counter < 8:
                print()

    else:
        print('No such letter in the word')
        counter += 1
        if counter < 8:
            print()

if ''.join(show_word) == word:
    print()
    print(''.join(show_word))
    print('You guessed the word!')
    print('You survived!')
else:
    print('You are hanged!')