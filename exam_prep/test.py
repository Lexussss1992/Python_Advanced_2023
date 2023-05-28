def blind_mans_buff_game(N, M, playground):
    player_position = None
    touched_opponents = 0
    moves_made = 0

    # Find the initial position of the player
    for i in range(N):
        for j in range(M):
            if playground[i][j] == 'B':
                player_position = (i, j)
                break

    # Game loop
    while True:
        command = input()

        if command == 'Finish':
            break

        new_position = None

        if command == 'up':
            new_position = (player_position[0] - 1, player_position[1])
        elif command == 'down':
            new_position = (player_position[0] + 1, player_position[1])
        elif command == 'left':
            new_position = (player_position[0], player_position[1] - 1)
        elif command == 'right':
            new_position = (player_position[0], player_position[1] + 1)

        if new_position is None:
            continue

        row, col = new_position

        if 0 <= row < N and 0 <= col < M:
            if playground[row][col] == 'O':
                continue
            elif playground[row][col] == 'P':
                touched_opponents += 1
                moves_made += 1
                playground[row][col] = '-'
                player_position = new_position
            elif playground[row][col] == '-':
                moves_made += 1
                player_position = new_position

    print("Game over!")
    print(f"Touched opponents: {touched_opponents} Moves made: {moves_made}")


# Test the game
N, M = map(int, input().split())

playground = []
for _ in range(N):
    row = list(input())
    playground.append(row)

blind_mans_buff_game(N, M, playground)