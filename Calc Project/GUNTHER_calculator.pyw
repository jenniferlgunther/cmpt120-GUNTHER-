# Jennifer Gunther
# Project 1 - Calculator
# 23 February 2018

from graphics import *
from GUNTHER_calculatorfunctions import *

win = GraphWin('Calculator', 320, 500)

displayTextElement = Text(Point(0, 50), "")

calcGrid = [
    [7, 8, 9, '/'],
    [4, 5, 6, '*'],
    [1, 2, 3, '-'],
    ['+/-', 0,'.','+'],
    ['', '', 'Del', '=']
]
buttons = [['','','',''],['','','',''],['','','',''],['','','',''],['','','','']]

def calcButton(x, y, value):
    button = Rectangle(Point(x,y),Point(x + 80,y + 80))
    button.setFill('lightpink')
    button.draw(win)
    text.setFace(courier)
    text.setSize(20)
    text = Text(Point(x + 40, y + 40), value)
    text.draw(win)
    return button

def inside(clicked, button):
    if clicked.getX() > button.p1.getX()and clicked.getX() < button.p2.getX():
            if clicked.getY() > button.p1.getY()and clicked.getY() < button.p2.getY():
                return True
    return False

def clickedButton(clicked):
    for i in range(5):
        for j in range(4):
            if clicked.getX() > buttons[i][j].p1.getX()and clicked.getX() < buttons[i][j].p2.getX():
                if clicked.getY() > buttons[i][j].p1.getY()and clicked.getY() < buttons[i][j].p2.getY():
                    return i, j
    return -1, -1

def createCalculatorButtons():
    for i in range(5):
        for j in range(4):
            buttons[i][j] = calcButton(j * 80, i * 80 + 100, calcGrid[i][j])


def main():
    createCalculatorButtons()
    displayString = ''
    displayTextElement = Text(Point(0, 50), "")
    displayTextElement.draw(win)
    op1 = 0
    op2 = 0
    opr = ""
    while 1 == 1:
        clicked = win.getMouse()
        print (clicked.getX(), clicked.getY())
        row, col = clickedButton(clicked)
        if row >= 0:
            buttons[row][col].setFill('blue')
            displayString = (displayString + str(calcGrid[row][col])).rjust(200);
            displayTextElement.undraw()
            displayTextElement = Text(Point(0, 50), displayString)
            displayTextElement.draw(win)
            print (calcGrid[row][col])
        for i in range(5):
            for j in range(4):
                if not(i == row and j == col):
                    buttons[i][j].setFill('lightpink')

main()


