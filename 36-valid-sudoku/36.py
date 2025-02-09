board =  [["5","3",".",".","7",".",".",".","."]
         ,["6",".",".","1","9","5",".",".","."]
         ,[".","9","8",".",".",".",".","6","."]
         ,["8",".",".",".","6",".",".",".","3"]
         ,["4",".",".","8",".","3",".",".","1"]
         ,["7",".",".",".","2",".",".",".","6"]
         ,[".","6",".",".",".",".","2","8","."]
         ,[".",".",".","4","1","9",".",".","5"]
         ,[".",".",".",".","8",".",".","7","9"]]

def isValidSodoku(board):
    for i in range(0,9):
        if not isValidMatrix(board,i,0,i,8):
              return False
        if not isValidMatrix(board,0,i,8,i):
            return False
    for i in range(0,3):
        if not isValidMatrix(board,0,0 + 3*i,2,2 + 3*i):
            return False
        if not isValidMatrix(board,3,0 + 3*i,5,2 + 3*i):
            return False
        if not isValidMatrix(board,6,0 + 3*i,8,2 + 3*i):
            return False
    return True

def isValidMatrix(board,x1,y1,x2,y2):
    numHash = {}
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            if board[i][j] != ".":
                if board[i][j] in numHash:
                    return False
                else:
                    numHash[board[i][j]] = True
    return True


print(isValidSodoku(board))                

# TODO Try with multi threading
