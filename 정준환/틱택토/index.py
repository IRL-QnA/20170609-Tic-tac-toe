def print_map(game_map=None):
    print('----Map----')
    for line in game_map:
        print(' {} | {} | {}'.format(line[0], line[1], line[2]))
    print('-----------')

def check_valid(x, y):
    available_value = ['0', '1', '2']
    if not (x in available_value and y in available_value):
        return False

    x = int(x)
    y = int(y)

    return game_map[y][x] == '.'

def bingos(mark):
    global game_map
    bingo = 0

    # horizontal
    for i in range(0, 3):
        for j in range(0, 3):
            if game_map[i][j] != mark:
                break
            if j == 2:
                bingo += 1

    # vertical
    for i in range(0, 3):
        for j in range(0, 3):
            if game_map[j][i] != mark:
                break
            if j == 2:
                bingo += 1
    # diagonal
    if game_map[1][1] == mark:
        if game_map[0][0] == game_map[2][2] == mark:
            bingo += 1

        if game_map[2][0] == game_map[0][2] == mark:
            bingo += 1

    return bingo

def game_start():
    # initiate game_map
    global game_map
    game_map = [
        ['.', '.', '.'],
        ['.', '.', '.'],
        ['.', '.', '.']
    ]
    # (empty:'.' / player1:'O' / player2:'X')

    isDraw = True

    print_map(game_map)
    for i in range(0, 9):
        player_num = i % 2 + 1

        while True:
            coordinate = input("Player" + str(player_num) + ": x y\n").split(' ')

            x = coordinate[0]

            # 띄어쓰기 없이 값을 입력했을때의 경우를 거르기 위한 조건문
            if len(coordinate) == 2:
                y = coordinate[1]

                if check_valid(x, y):
                    x = int(x)
                    y = int(y)
                    break

            print(">>> 유효하지 않은 값입니다. x, y값으로 0부터 2사이의 값을 입력해 주십시오.\n")


        if player_num == 1:
            mark_type = 'O'
        else:
            mark_type = 'X'

        game_map[y][x] = mark_type
        print_map(game_map)

        b = bingos(mark_type)

        if b == 1:
            isDraw = False
            print("Player" + str(player_num) + " won the game!")
            break

        elif b == 0:
            continue

        else:
            break

    if isDraw:
        print("Draw!")

    if input("\n>>> 게임을 계속하려면 Enter키를 눌러주세요.\n") == '':
        return True
    else:
        return False

game_map = [
    ['.', '.', '.'],
    ['.', '.', '.'],
    ['.', '.', '.']
]
while True:
    if not game_start():
        break