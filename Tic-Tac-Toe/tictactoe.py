entrada = input('Enter cells: ').replace('_', ' ')

M = [[entrada[6], entrada[3], entrada[0]], [entrada[7], entrada[4], entrada[1]], [entrada[8], entrada[5], entrada[2]]]
print('---------')
print(f'| {M[0][2]} {M[1][2]} {M[2][2]} |')
print(f'| {M[0][1]} {M[1][1]} {M[2][1]} |')
print(f'| {M[0][0]} {M[1][0]} {M[2][0]} |')
print('---------')
teste = True
while teste:
    aux = input('Enter the coordinates: ').split(' ')
    if not aux[0].isdigit():
        print('You should enter numbers!')
        teste = True
    elif int(aux[0]) > 3 or int(aux[1]) > 3:
            print('Coordinates should be from 1 to 3!')
            # aux = input('Enter the coordinates: ').split(' ')
            teste = True
    elif M[int(aux[0]) - 1][int(aux[1]) - 1] != ' ':
            print('This cell is occupied! Choose another one!')
            # aux = input('Enter the coordinates: ').split(' ')
            teste = True
    elif M[int(aux[0]) - 1][int(aux[1]) - 1] == ' ':
            M[int(aux[0]) - 1][int(aux[1]) - 1] = 'X'
            teste = False
print('---------')
print(f'| {M[0][2]} {M[1][2]} {M[2][2]} |')
print(f'| {M[0][1]} {M[1][1]} {M[2][1]} |')
print(f'| {M[0][0]} {M[1][0]} {M[2][0]} |')
print('---------')

# position = input()
#
# print('---------')
# print(f'| {position[0]} {position[1]} {position[2]} |')
# print(f'| {position[3]} {position[4]} {position[5]} |')
# print(f'| {position[6]} {position[7]} {position[8]} |')
# print('---------')
# under = [entrada for entrada in position if entrada == '_']
# xis = [entrada for entrada in position if entrada == 'X']
# os = [entrada for entrada in position if entrada == 'O']
# # print(under, xis, os)
# if position[0] == position[1] == position[2] and position[3] == position[4] == position[5]:
#     print('Impossible')
# elif position[0] == position[1] == position[2] and position[6] == position[7] == position[8]:
#     print('Impossible')
# elif position[3] == position[4] == position[5] and position[6] == position[7] == position[8]:
#     print('Impossible')
# elif position[0] == position[3] == position[6] and position[1] == position[4] == position[7]:
#     print('Impossible')
# elif position[3] == position[4] == position[5] and position[2] == position[5] == position[8]:
#     print('Impossible')
# elif position[3] == position[4] == position[5] and position[2] == position[5] == position[8]:
#     print('Impossible')
# elif len(xis) - len(os) >= 2 or len(os) - len(xis) >= 2:
#     print('Impossible')
#
# elif position[0] == position[1] == position[2]:
#     print(f'{position[0]} wins')
# elif position[3] == position[4] == position[5]:
#     print(f'{position[0]} wins')
# elif position[6] == position[7] == position[8]:
#     print(f'{position[0]} wins')
# elif position[0] == position[4] == position[8]:
#     print(f'{position[0]} wins')
# elif position[6] == position[4] == position[2]:
#     print(f'{position[2]} wins')
# elif position[0] == position[3] == position[6]:
#     print(f'{position[2]} wins')
# elif position[1] == position[4] == position[7]:
#     print(f'{position[2]} wins')
# elif position[2] == position[5] == position[8]:
#     print(f'{position[2]} wins')
# elif len(under) >= len(xis) or len(under) >= len(os) and position[0] != position[1]:
#     print('Game not finished')
# elif len(under) >= len(xis) or len(under) >= len(os) and position[4] != position[5]:
#     print('Game not finished')
# elif len(under) >= len(xis) or len(under) >= len(os) and position[7] != position[8]:
#     print('Game not finished')
# elif len(under) >= len(xis) or len(under) >= len(os) and position[0] != position[1]:
#     print('Game not finished')
#
# else:
#     print('Draw')
