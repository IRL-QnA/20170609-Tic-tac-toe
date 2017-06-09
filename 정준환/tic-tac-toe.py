def print_map(game_map=None):
    print('----Map----')
    for line in game_map:
        print(' {} | {} | {}'.format(line[0], line[1], line[2]))
    print('-----------')

def check_valid(x, y):
    if x < 0 or x > 2 or y < 0 or y > 2:
        return False

    return game_map[y][x] == '.'

def bingos(mark):
    bingo = 0
    # horizontal
    for i in range (0, 3):
        for j in range (0, 3):
            if game_map[i][j] != mark:
                break
            if j == 2: bingo += 1

    # vertical
    for i in range (0, 3):
        for j in range (0, 3):
            if game_map[j][i] != mark:
                break
            if j == 2: bingo += 1
    # diagonal
    if game_map[1][1] == mark:
        if game_map[0][0] == game_map[2][2] == mark:
            bingo += 1

        if game_map[2][0] == game_map[0][2] == mark:
            bingo += 1
    
    return bingo

game_map = [['.', '.', '.'],['.', '.', '.'],['.', '.', '.']]
# (empty:'.' / player1:'O' / player2:'X')

for i in range(0, 9):
    player_num = i % 2 + 1

    while True:
        coordinate = input("Player" + str(player_num) + ": x y\n").split(' ')

        # todo : 좌표값으로 정수형 외의 자료형을 넣었을때의 에러 처리
        x = int(coordinate[0])
        y = int(coordinate[1])

        if check_valid(x, y): break

        print(">>>유효하지 않은 값입니다.\n")


    if player_num == 1:
        mark_type = 'O'
    else:
        mark_type = 'X'

    game_map[y][x] = mark_type
    print_map(game_map)

    b = bingos(mark_type)
    if b == 1:
        print("Player" + str(player_num) + " won the game!")
        break
        
    elif b == 0:
        continue

    else:
        print("Draw!")