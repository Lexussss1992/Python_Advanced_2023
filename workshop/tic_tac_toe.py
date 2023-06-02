from math import ceil


def setup():
    global player_one, player_two
    player_one_name = input('Player one name: ')
    player_two_name = input('Player two name: ')
    player_one_sign = input(f'{player_one_name} would you like to play with "X" or "O"? ')
    player_two_sign = 'X' if player_one_sign == 'O' else 'O'
    player_one = [player_one_name, player_one_sign]
    player_two = [player_two_name, player_two_sign]
    print('This is numeration of the board: ')
    print('| 1 | 2 | 3 |')
    print('| 4 | 5 | 6 |')
    print('| 7 | 8 | 9 |')
    print(f'{player_one_name} starts first!')


def play(current, board):
    global counter_for_draw
    while True:
        try:
            choice = int(input(f'{current[0]} choose a free position [1-9]: '))
            row = ceil(choice / 3) - 1
            col = choice % 3 - 1
            if not 0 < choice <= 9:
                print('Please enter a valid number.')
                continue
            if board[row][col] == ' ':
                board[row][col] = current[1]
                draw_board(board)
                check_if_won(current, board)
                return False
            else:
                continue

        except ValueError:
            print('Please enter a valid number.')


def draw_board(board):
    for row in board:
        print('|  ', end='')
        print('  |  '.join([str(x) for x in row]), end='')
        print('  |')


def check_if_won(current, board):
    global loop
    first_row = all([x == current[1] for x in board[0]])
    second_row = all([x == current[1] for x in board[1]])
    third_row = all([x == current[1] for x in board[2]])
    first_column = all(x == current[1] for x in [board[0][0], board[1][0], board[2][0]])
    second_column = all(x == current[1] for x in [board[0][1], board[1][1], board[2][1]])
    third_column = all(x == current[1] for x in [board[0][2], board[1][2], board[2][2]])
    first_diagonal = all(x == current[1] for x in [board[0][0], board[1][1], board[2][2]])
    second_diagonal = all(x == current[1] for x in [board[2][0], board[1][1], board[0][2]])
    if any([first_row, second_row, third_row, first_column, second_column, third_column, first_diagonal, second_diagonal]):
        print(f'{current[0]} won!')
        loop = False
    if counter_for_draw == 9:
        print('Draw!')
        raise SystemExit


user_choice = input('Do you want to play (Y/N): ')

while user_choice == 'Y':
    if user_choice in ('Y', 'N'):
        if user_choice == 'Y':
            player_one = None
            player_two = None
            board = [[x for x in [' ' for _ in range(3)]] for _ in range(3)]
            setup()
            current = player_one
            other = player_two
            loop = True
            counter_for_draw = 0

            while loop:
                counter_for_draw += 1
                play(current, board)
                current, other = other, current
        else:
            print('Bye')
            break
        user_choice = input('Do you want to play (Y/N): ')
    else:
        input('Enter a valid option (Y/N): ')
        continue
else:
    input('Enter a valid option (Y/N): ')