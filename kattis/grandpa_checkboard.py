from sys import stdin


def grandpa(board):
    for i in range(len(board)):
        white, black = 0, 0
        seq, start = 0, board[i][0]
        for j in range(len(board[0])):
            if seq >= 3: return 0
            if board[i][j] == 'W': white += 1
            else: black += 1
            if start == 'W' and board[i][j] == 'W': seq += 1
            elif start == 'B' and board[i][j] == 'B': seq += 1
            else:
                start = board[i][j]
                seq = 1
        if white != black: return 0 
         
    for j in range(len(board[0])):
        white, black = 0, 0
        seq, start = 0, board[0][j]
        for i in range(len(board)):
            if seq >= 3: return 0
            if board[i][j] == 'W': white += 1
            else: black += 1
            if start == 'W' and board[i][j] == 'W': seq += 1
            elif start == 'B' and board[i][j] == 'B': seq += 1
            else:
                start = board[i][j]
                seq = 1
        if white != black: return 0
    return 1


n = int(input())
board = []
for i in range(n):
    row = list(stdin.readline().rstrip())
    board.append(row)
print(grandpa(board))