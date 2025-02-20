def printboard(board):
    for row in board:
        print(" | ".join(row))
        print("-"*10)

def iswinner(board, player):
    
    return (any(all(board[i][j] for j in range(3))for i in range(3))
            or any(all(board[j][i] for j in range(3))for i in range(3))
            or all(board[i][i] for i in range(3))
            or all(board[i][2-i]for i in range(3)))

def isfull(board):
    for i in range(3):
        for j in range(3):
            if board[i][j]==' ':
                return False
    return True


def minimax(board,maximizing):
    if iswinner(board,'X'):return -1
    if iswinner(board,'O'):return 1
    if isfull(board):return 0
    
    best=float('-inf') if maximizing else float('inf')
    for i in range(3):
        for j in range(3):
            if board[i][j]==' ':
                board[i][j]='O' if maximizing else 'X'
                score=minimax(board,False)
                board[i][j]=' '
                best=max(best,score) if maximizing else min(best,score)
    return best
        
def getbestmove(board):
    bestmove,bestscore=None,float('-inf')
    
    for i in range(3):
        for j in range(3):
            if board[i][j]==' ':
                board[i][j]='O'
                score=minimax(board,False)
                board[i][j]=' '
                if score>bestscore:
                    bestmove,bestscore=(i,j),score
    return bestmove

def playgame():
    board=[[' 'for _ in range(3)] for _ in range(3)]
    
    while not iswinner(board,'X') and not iswinner(board,'O') and not isfull(board):
        printboard(board)
        row=int(input("Enter row: "))
        col=int(input("Enter col: "))
        if board[row][col]==' ':
            board[row][col]='X'
        else:
            print("Inavlid")
            continue
        
        if not isfull(board) and not iswinner(board,'X'):
            move=getbestmove(board)
            board[move[0]][move[1]]='O'
    
    printboard(board)
    if iswinner(board,'X'):
         print("You wins")
         
    elif iswinner(board,'O'):
        print("AI wins")
    else:
        print("Draw")
playgame()