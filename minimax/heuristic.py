def get_opponent(player):
    return 2 if player == 1 else 1


def get_heuristic(board, player):
    player_score = 0
    opponent_score = 0
    board_copy = [[[0, 0] for _ in board[0]] for _ in board]
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] == player:
                board_copy[y][x][0] = (
                    max(
                        board_copy[max(0, y - 1)][x][0],
                        board_copy[y][max(0, x - 1)][0],
                        board_copy[max(0, y - 1)][max(0, x - 1)][0],
                    )
                    + 1
                )
            elif board[y][x] == get_opponent(player):
                board_copy[y][x][1] = (
                    max(
                        board_copy[max(0, y - 1)][x][1],
                        board_copy[y][max(0, x - 1)][1],
                        board_copy[max(0, y - 1)][max(0, x - 1)][1],
                    )
                    + 1
                )
    for y in range(len(board_copy)):
        for x in range(len(board_copy[0])):
            player_score = max(player_score, board_copy[y][x][0])
            opponent_score = max(opponent_score, board_copy[y][x][1])

    return player_score - opponent_score
