# Write your code here
import random

word = random.choice(['python', 'java', 'kotlin', 'javascript'])
hidden_word = word[:3] + '-' * (len(word)-3)
# for i in range(len(word)):
#     if i < 3:
#         hidden_word += word[i]
#     else:
#         hidden_word += '-'
print('H A N G M A N')
guess_word = input(f'Guess the word {hidden_word}:')
if guess_word == word:
    print('You survived!')
else:
    print('You are hanged!')