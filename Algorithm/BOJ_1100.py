chess_board = [list(input()) for _ in range(8)]

count = 0

for i in range(8):
    if i%2==0:
        chess_board[i]=chess_board[i][::-1]
    for j in range(8):
        if j%2==1 and chess_board[i][j] =='F':
            count += 1
    
print(count)