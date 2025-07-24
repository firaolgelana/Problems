# Problem: Where's the Bishop? - https://codeforces.com/problemset/problem/1692/C

for _ in range(int(input())):
    input()  
    board = [input() for _ in range(8)]
    
    for r in range(1, 7):  
        for c in range(1, 7):
            if board[r][c] == '#' and \
               board[r-1][c-1] == '#' and \
               board[r-1][c+1] == '#' and \
               board[r+1][c-1] == '#' and \
               board[r+1][c+1] == '#':
                print(r + 1, c + 1) 
                break
