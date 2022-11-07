EMPTY = "-"
ROOK = "ROOK"
board = []

board = [[EMPTY for i in range(8)] for j in range(8)]
'''for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)'''

board[0][0] = ROOK
board[0][7] = ROOK
board[7][0] = ROOK
board[7][7] = ROOK

for i in range(8):
    print(board[i])

t = [[3-i for i in range(3)] for j in range (3)]
s=0
for i in range(3):
    s+= t[i][i]
print(s)

for i in range(1):
    print("#")
else:
    print('#')