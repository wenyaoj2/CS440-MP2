board=[['X','_','_','_','_','_','_','_','_'],
        ['_','O','_','_','_','_','_','_','_'],
        ['_','_','X','_','_','_','_','_','_'],
        ['_','_','_','_','_','_','_','_','_'],
        ['_','_','_','_','_','_','_','_','_'],
        ['_','_','_','_','_','_','_','_','_'],
        ['_','_','_','_','_','O','_','_','_'],
        ['_','_','_','X','O','X','X','_','_'],
        ['_','_','_','O','_','_','_','_','_']]
print(board[1][0])
globalIdx=[(0,0),(0,3),(0,6),(3,0),(3,3),(3,6),(6,0),(6,3),(6,6)]
x = 'X'
y = 'X'
print(x+y)
def checkWinner():
        #Return termimnal node status for maximizer player 1-win,0-tie,-1-lose
        """
        This function checks whether there is a winner on the board.
        output:
        winner(int): Return 0 if there is no winner.
                     Return 1 if maxPlayer is the winner.
                     Return -1 if miniPlayer is the winner.
        """
        #YOUR CODE HERE
        winner=0
        for i in globalIdx:
            for j in range(3):
                if(board[i[0]+j][i[1]]+board[i[0]+j][i[1]+1]+board[i[0]+j][i[1]+2]=="XXX"):
                    winner = 1
                    return winner
                elif(board[i[0]+j][i[1]]+board[i[0]+j][i[1]+1]+board[i[0]+j][i[1]+2]=="OOO"):
                    winner = -1
                    return winner
                elif(board[i[0]][i[1]+j]+board[i[0]+1][i[1]+j]+board[i[0]+2][i[1]+j]=="XXX"):
                    winner = 1
                    return winner
                elif(board[i[0]][i[1]+j]+board[i[0]+1][i[1]+j]+board[i[0]+2][i[1]+j]=="OOO"):
                    winner = -1
                    return winner
            if(str(board[i[0]][i[1]]+board[i[0]+1][i[1]+1]+board[i[0]+2][i[1]+2])=="XXX"or str(board[i[0]+2][i[1]]+board[i[0]+1][i[1]+1]+board[i[0]][i[1]+2])=="XXX"):
                winner = 1
                return winner
            elif(board[i[0]][i[1]]+board[i[0]+1][i[1]+1]+board[i[0]+2][i[1]+2]=="OOO"or board[i[0]+2][i[1]]+board[i[0]+1][i[1]+1]+board[i[0]][i[1]+2]=="OOO"):
                winner = -1
                return winner
        return 0
print(checkWinner())
