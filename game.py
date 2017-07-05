square = ['_', '_', '_', '_', '_', '_', '_', ' ', ' ', ' ']
# trace = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
player_1 = input('enter player 1 name :\n')
player_2 = input('enter player 2 name :\n')
r = 0
t = 0


def begin():
    board()
    r = 0
    t = 0
    while r == 0:
        mark_1 = int(input('enter the place to mark ' + player_1))
        if (mark_1 <= 9 | mark_1 >= 1) :
            square[mark_1] = 'o'
            # trace[t] = mark_1
            t = t+1
            board()
            r = win()
            if t == 9:
                print('draw')
                t = 0
                r = 2
                for i in range(1, 7):
                    square[i] = '_'
                square[7] = square[8] = square[9] = ' '
                if (input('play again?(y/n)') == 'y'):
                    begin()
                else:
                    break
            if r == 1:
                print(player_1+' '+'won')
                if (input('play again?(y/n)') == 'y'):
                    begin()
                else:
                    break
        else:
            print('invalid input\n')
            mark_1 = int(input('enter the place to mark ' + player_1))

        mark_2 = int(input('enter the place to mark ' + player_2))
        if (mark_2 <= 9 | mark_2 >= 1):
            square[mark_2] = 'x'
            # trace[t] = mark_2
            t = t + 1
            board()
            r = win()
            if r == 1:
                print(player_2+' '+'won')
                if(input('play again?(y/n)') == 'y'):
                    begin()
                else:
                    break
            if t == 9:
                print('draw')
                t = 0
                r = 2
                for i in range(1, 7):
                    square[i] = '_'
                square[7] = square[8] = square[9] = ' '
                if (input('play again?(y/n)') == 'y'):
                    begin()
                else:
                    break
        else:
            print('invalid input\n')
            mark_2 = int(input('enter the place to mark ' + player_2))


def win():
    r = 0
    if (square[1] == square[2] == square[3] == 'o') | (square[1] == square[2] == square[3] == 'x'):
        for i in range(1,7):
            square[i] = '_'
        square[7] = square[8] = square[9] = ' '
        r = 1
    elif (square[4] == square[5] == square[6] == 'o') | (square[4] == square[5] == square[6] == 'x'):
        for i in range(1,7):
            square[i] = '_'
        square[7] = square[8] = square[9] = ' '
        r = 1
    elif (square[7] == square[8] == square[9] == 'o') | (square[7] == square[8] == square[9] == 'x'):
        for i in range(1,7):
            square[i] = '_'
        square[7] = square[8] = square[9] = ' '
        t = 0
        r = 1
    elif (square[1] == square[4] == square[7] == 'o') | (square[1] == square[4] == square[7] == 'x'):
        for i in range(1,7):
            square[i] = '_'
        square[7] = square[8] = square[9] = ' '
        t = 0
        r = 1
    elif (square[2] == square[5] == square[8] == 'o') | (square[2] == square[5] == square[8] == 'x'):
        for i in range(1,7):
            square[i] = '_'
        square[7] = square[8] = square[9] = ' '
        t = 0
        r = 1
    elif (square[3] == square[6] == square[9] == 'o') | (square[3] == square[6] == square[9] == 'x'):
        for i in range(1,7):
            square[i] = '_'
        square[7] = square[8] = square[9] = ' '
        t = 0
        r = 1
    elif (square[1] == square[5] == square[9] == 'o') | (square[1] == square[5] == square[9] == 'x'):
        for i in range(1,7):
            square[i] = '_'
        square[7] = square[8] = square[9] = ' '
        t = 0
        r = 1
    elif (square[3] == square[5] == square[7] == 'o') | (square[3] == square[5] == square[7] == 'x'):
        for i in range(1,7):
            square[i] = '_'
        square[7] = square[8] = square[9] = ' '
        t = 0
        r = 1
    else:
        r = 0

    return r


def board():
    print('     '+square[1] + '|' + square[2] + '|' + square[3])
    print('     ' + square[4] + '|' + square[5] + '|' + square[6])
    print('     ' + square[7] + '|' + square[8] + '|' + square[9])

begin()