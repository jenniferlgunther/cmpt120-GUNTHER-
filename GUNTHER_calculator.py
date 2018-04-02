# Jennifer Gunther
# Project 1 - Calculator
# 23 February 2018

from graphics import *
from GUNTHER_calculatorfunctions import *

buttons = []

def create_button(win, x1, y1, x2, y2, label, color = 'lightpint'):
    button = Rectangle(Point(x1,y1), Point(x2,y2))
    button.setFill(color)
    button.draw(win)
    text = Text(button.getCenter(), label)
    text.setFace('courier')
    text.setSize('20')
    text.draw(win)
    return button, label

def apply_button(button, label, x, y):
    x1 = button.p1.getX()
    y1 = button.p1.getY()
    x2 = button.p2.getX()
    y2 = button.p2.getY()
    if x > x1 and x < x2 and y > y1 and y < y2:
        return label
    return False

def do_calculation(answer, entry, operation):
    print ("do calculation")
    print (operation)
    if answer == None:
        answer = entry
        entry = 0
    else:
        if operation == '+':
            answer = add(answer, entry)
            print ("add")
        elif operation == '-':
            answer = subtract(answer, entry)
            print ("subtract")
        elif operation == '*':
            answer = multiply(answer, entry)
            print ('multiply')
        elif operation == '/':
            answer = divide(answer, entry)
            print ('divide')
        elif operation == '+/-':
            answer = change_sign(answer)
            print ('change sign')
        elif operation == 'x2':
            answer = square(answer)
            print ('squared')
        entry = 0
    return answer, entry


def main():
    win = GraphWin("Calculator", 300, 500)

    displayScreen = Rectangle (Point(10,10), Point(290,110))
    displayScreen.setFill('lightcyan')
    displayScreen.draw(win)

    buttons.append(create_button (win, 8, 115, 73, 187, "7"))
    buttons.append(create_button (win, 8, 192, 73, 264, "4"))
    buttons.append(create_button (win, 8, 269, 73, 341, "1"))
    buttons.append(create_button (win, 8, 346, 73, 418, "+/-", 'blue'))
    buttons.append(create_button (win, 8, 423, 73, 495, "x2", 'blue'))
    buttons.append(create_button (win, 81, 115, 146, 187, "8"))
    buttons.append(create_button (win, 81, 192, 146, 264, "5"))
    buttons.append(create_button (win, 81, 269, 146, 341, "2"))
    buttons.append(create_button (win, 81, 346, 146, 418, "0"))
    buttons.append(create_button (win, 81, 423, 146, 495, ""))
    buttons.append(create_button (win, 154, 115, 219, 187, "9"))
    buttons.append(create_button (win, 154, 192, 219, 264, "6"))
    buttons.append(create_button (win, 154, 269, 219, 341, "3"))
    buttons.append(create_button (win, 154, 346, 219, 418, ""))
#TODO add decimal to blank button
    buttons.append(create_button (win, 154, 423, 219, 495, "C", 'blue'))
    buttons.append(create_button (win, 227, 115, 292, 187, "/", 'blue'))
    buttons.append(create_button (win, 227, 192, 292, 264, "*", 'blue'))
    buttons.append(create_button (win, 227, 269, 292, 341, "+", 'blue'))
    buttons.append(create_button (win, 227, 346, 292, 418, "-", 'blue'))
    buttons.append(create_button (win, 227, 423, 292, 495, "=", 'blue'))

    displayString = ''
    displayTextElement = Text(Point(200, 50), "")
    displayTextElement.draw(win)
#answer is running total
#entry is the current number being typed in
#operation is adding the math funtion to the equals display
    answer = None
    entry = 0
    operation = None


    while 1 == 1:
        clicked = win.getMouse()
        x = clicked.getX()
        y = clicked.getY()
        print(x, y)

    for b in buttons:
        button, label = b
        key = check_button(button, label, x, y)
        if key:
            print ("button pressed: %s" % key)
            if key == '=':
                   # do the calculation
                if answer == None:
                       answer = entry
                       displayString = str(answer)
                       entry = 0
               # JA: Which if should this else match?
               #else:
               #    answer, entry = do_calculation(answer, entry, operation)
               #    operation = None
               #  displayString = str(answer)

               # print ("calculate")
            elif key in ['+', '-', '/', '*']:
                 # do the calculation
                   answer, entry = do_calculation(answer, entry, operation)
                   operation = key
                   displayString = str(answer)

            elif key == '+/-':
                    # do the calculation
                    answer, entry = do_calculation(answer, entry, key)
                    displayString = str(answer)

            elif key == 'C':
                    # clear current text
                    displayString = ''
                    answer = None
                    entry = 0
                    operation = None

            else:
                    # number keys
                    entry = (entry * 10) + int(key)
                    displayString = str(entry)

                    displayTextElement.undraw()
                    displayTextElement = Text(Point(200, 50), displayString)
                    displayTextElement.setFace('arial')
                    displayTextElement.setSize(20)
                    displayTextElement.draw(win)


                    print('answer: %s entry: %s display: %s' % (answer, entry, displayString))

main()

