import itertools


BS = 5 # board size


def calculate_score(checked, board, just_checked):
    return sum(board[i][j] for i in range(BS) for j in range(BS) if checked[i][j] == 0) * just_checked


def check_if_win(checked, i, j):
    return sum(checked[i]) == BS or sum(checked[i][j] for i in range(BS)) == BS


def play(numbers, boards):
    boards_cnt = len(boards)
    won_boards_cnt = 0
    won_boards = [0]*boards_cnt

    for num in numbers:
        for b_i, board in enumerate(boards):
            if won_boards[b_i] == 0 and num in board[1]:
                i, j = board[1][num]
                board[2][i][j] = 1
                if check_if_win(board[2], i, j):
                    won_boards[b_i] = 1
                    won_boards_cnt += 1
                    if won_boards_cnt == boards_cnt:
                        return calculate_score(board[2], board[0], num)


with open('4_i.txt') as f:
    A = f.read().splitlines()
    numbers = map(int, A[0].split(','))
    boards = []

    i = 2
    while i < len(A):
        curr_board = []

        while A[i] != '':
            curr_board.append(list(map(int, A[i].split())))
            i += 1
            if i == len(A):
                break

        board_dict = {curr_board[i][j]: (i, j) for i in range(BS) for j in range(BS)}
        checked = [[0 for _ in range(BS)] for _ in range(BS)]

        boards.append((curr_board, board_dict, checked))
        i += 1


print(play(numbers, boards))
