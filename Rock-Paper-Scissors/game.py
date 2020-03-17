# Write your code here
from random import choice

jokenpo = ''
rating = []
player = {}
point = 0
file = open('rating.txt', 'r', encoding='utf-8')
lista = file.read().split('\n')
# print(lista)
for v,i in enumerate(lista):
    if len(i) > 1:
        player["name"], player["point"] = i.split(" ")
        # print(player["name"], player["point"])
        rating.append(player.copy())
        player.clear()

def default_game():
    global point
    while True:
        jokenpo = input(' ')
        computer = choice(['rock', 'scissors', 'paper'])

        if jokenpo == "!exit":
            break
        if jokenpo == computer:
            print(f'There is a draw ({computer})')
            point += 50
        elif jokenpo == 'scissors' and computer == 'paper':
            print(f'Well done. Computer chose {computer} and failed')
            point += 100
        elif jokenpo == 'paper' and computer == 'rock':
            print(f'Well done. Computer chose {computer} and failed')
            point += 100
        elif jokenpo == 'rock' and computer == 'scissors':
            print(f'Well done. Computer chose {computer} and failed')
            point += 100
        elif jokenpo == "!rating":
            print(f'Your rating: {point}')
        else:
            print(f'Sorry, but computer chose {computer}')
    print('Bye!')

file.close()
# print(len(lista))
name = input("Enter your name: ")

if len(lista) < 2:
    player['name'] = name
    player['point'] = 0
    rating.append(player.copy())
    player.clear()
for i in range(len(rating)):
    if (rating[i]["name"]) == name:
        point += int(rating[i]["point"])
        break
    else:
        # print("entou else")
        player['name'] = name
        player['point'] = 0
        rating.append(player.copy())
        player.clear()
        break
print(f'Hello, {name}')
options = input().split(',')
print("Okay, let's start")
if len(options) < 2:
    default_game()
# print(options)
options_one = options[:round(len(options)/2+0.5)]
options_two = options[round(len(options)/2+0.5):]
# print(options_one)
# print(options_two)
while True:
    computer = choice(options)
    # print(computer)
    jokenpo = input(' ')
    if jokenpo == "!exit":
        break
    if jokenpo == computer:
        print(f'There is a draw ({computer})')
        point += 50
    if jokenpo == "!rating":
        print(f'Your rating: {point}')
    elif jokenpo in options_one and computer in options_one:
        # print('options one')
        if options_one.index(jokenpo) > options_one.index(computer):
            print(f'Well done. Computer chose {computer} and failed')
            point += 100
        else:
            print(f'Sorry, but computer chose {computer}')
    elif jokenpo in options_two and computer in options_two:
        # print("options two")
        if options_two.index(jokenpo) > options_two.index(computer):
            print(f'Well done. Computer chose {computer} and failed')
            point += 100
        else:
            print(f'Sorry, but computer chose {computer}')
    elif jokenpo in options_one and computer in options_two:
        # print('options one and two')
        print(f'Well done. Computer chose {computer} and failed')
        point += 100

    # elif jokenpo == 'paper' and computer == 'rock':
    #     print(f'Well done. Computer chose {computer} and failed')
    #     point += 100
    # elif jokenpo == 'rock' and computer == 'scissors':
    #     print(f'Well done. Computer chose {computer} and failed')
    #     point += 100

    else:
        print(f'Sorry, but computer chose {computer}')
print('Bye!')

for i in range(len(rating)):
    if (rating[i]["name"]) == name:
        rating[i]["point"] = point

file = open('rating.txt', 'w', encoding='utf-8')
for i in range(len(rating)):
    file.write(str(rating[i]["name"]))
    file.write(" ")
    file.write(str(rating[i]["point"]))
    file.write("\n")
file.close()
