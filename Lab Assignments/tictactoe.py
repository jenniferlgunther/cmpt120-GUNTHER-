# Introduction to Programming
# Jennifer Gunther
#  30 March 2018

symbol = [ " ", "x", "o"]

def printRow(row):
    one=' '
    two=' '
    three=' '
    if row[0]==1:
        one='o'
    if row[0]==2:
        one='x'
    if row[1]==1:
        two='o'
    if row[1]==2:
        two='x'
    if row[2]==1:
        three='o'
    if row[2]==2:
        three='x'
    print("| " + one + " | " + two + " | " + three + " |")

def lining():
    print("+-----------+")

def printBoard(board):
    lining()
    printRow(board[0])
    lining()
    printRow(board[1])
    lining()
    printRow(board[2])
    lining()

def markBoard(board, row, col, player):
    board[row][col]=player

def getPlayerMove():
    row = int(input("Please enter a row number."))
    col = int(input("Please enter a column number."))
    return row,col

def hasBlanks(board):
    for i in range(3):
        for k in range(3):
            if board[i][k]==0:
                return True
    return False

def main():
    board = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]
    player = 1
    while hasBlanks(board):
        printBoard(board)
        row,col = getPlayerMove()
        markBoard(board, row, col, player)
        player = player % 2 + 1
    printBoard(board)


main()
        
