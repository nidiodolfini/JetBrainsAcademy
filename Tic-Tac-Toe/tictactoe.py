entrada = '_________'.replace('_', ' ')

M = [[entrada[6], entrada[3], entrada[0]], [entrada[7], entrada[4], entrada[1]], [entrada[8], entrada[5], entrada[2]]]
print('---------')
print(f'| {M[0][2]} {M[1][2]} {M[2][2]} |')
print(f'| {M[0][1]} {M[1][1]} {M[2][1]} |')
print(f'| {M[0][0]} {M[1][0]} {M[2][0]} |')
print('---------')
teste = True
counter = 0
# while teste:
while counter < 10:
    aux = input('Enter the coordinates: ').split(' ')
    if not aux[0].isdigit():
        print('You should enter numbers!')
        # teste = True
    elif int(aux[0]) > 3 or int(aux[1]) > 3:
        print('Coordinates should be from 1 to 3!')
        # aux = input('Enter the coordinates: ').split(' ')
        # teste = True
    elif M[int(aux[0]) - 1][int(aux[1]) - 1] != ' ':
        print('This cell is occupied! Choose another one!')
        # aux = input('Enter the coordinates: ').split(' ')
        # teste = True
    elif M[int(aux[0]) - 1][int(aux[1]) - 1] == ' ':
        # print(counter)
        if counter % 2 == 0:
            M[int(aux[0]) - 1][int(aux[1]) - 1] = 'X'
            counter += 1
        else:
            M[int(aux[0]) - 1][int(aux[1]) - 1] = 'O'
            counter += 1

        print('---------')
        print(f'| {M[0][2]} {M[1][2]} {M[2][2]} |')
        print(f'| {M[0][1]} {M[1][1]} {M[2][1]} |')
        print(f'| {M[0][0]} {M[1][0]} {M[2][0]} |')
        print('---------')
        if M[0][0] == M[1][0] == M[2][0] and ((M[0][0] != ' ') or (M[1][0] != ' ') or (M[2][0] != ' ')):
            print(f'{M[0][0]} wins')
            break
        elif M[0][1] == M[1][1] == M[2][1] and ((M[0][1] != ' ') or (M[1][1] != ' ') or (M[2][1] != ' ')):
            print(f'{M[0][1]} wins')
            break
        elif M[0][2] == M[1][2] == M[2][2] and ((M[0][2] != ' ') or (M[1][2] != ' ') or (M[2][2] != ' ')):
            print(f'{M[0][2]} wins')
            break
        elif M[0][0] == M[0][1] == M[0][2] and ((M[0][0] != ' ') or (M[0][1] != ' ') or (M[0][2] != ' ')):
            print(f'{M[0][0]} wins')
            break
        elif M[1][0] == M[1][1] == M[1][2] and ((M[1][0] != ' ') or (M[1][1] != ' ') or (M[1][2] != ' ')):
            print(f'{M[1][0]} wins')
            break
        elif M[2][0] == M[2][1] == M[2][2] and ((M[2][0] != ' ') or (M[2][1] != ' ') or (M[2][2] != ' ')):
            print(f'{M[2][0]} wins')
            break
        elif M[0][2] == M[1][1] == M[2][0] and ((M[0][2] != ' ') or (M[1][1] != ' ') or (M[2][0] != ' ')):
            print(f'{M[0][2]} wins')
            break
        elif M[0][0] == M[1][1] == M[2][2] and ((M[0][0] != ' ') or (M[1][1] != ' ') or (M[2][2] != ' ')):
            print(f'{M[0][0]} wins')
            break
        elif counter == 9:
            print('Draw')
            break
