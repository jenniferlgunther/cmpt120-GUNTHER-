# Introduction to Programming
# Jennifer Gunther
#  30 March 2018

symbol = [ " ", "x", "o"]

def printRow(row):
    one=' '
    two=' '
    three=' '
    if row(0)==1:
        one='o'
    if row(0)==2:
        one='x'
    if row(1)==1:
        two='o'
    if row(1)==2:
        two='x'
    if row(2)==1:
        three='o'
    if row(2)==2:
        three='x'
    print("| " + one + " | " + two + " | " + three + " |")
    pass

def lining():
    print("+-----------+")
    pass

def printBoard(board):
    print(lining())
    print(printRow(board[0]))
    print(lining())
    print(printRow(board[1]))
    print(lining())
    print(printRow(board[2]))
    print(lining())
    pass

def markBoard(board, row, col, player):
    board[row][col]=player
    pass
