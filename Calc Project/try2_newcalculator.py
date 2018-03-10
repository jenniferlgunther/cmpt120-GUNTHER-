# This is a second attempt at the entire calculator project; part 1 and part 2

from GUNTHER_calculatorfunctions import *
from graphics import *

# calculator buttons (button, label)
buttons = []

def create_button(win, x1, y1, x2, y2, label, color = 'pink'):
    button = Rectangle(Point(x1, y1), Point(x2,y2))
    button.setFill(color)
    button.draw(win)
    text = Text(button.getCenter(), label)
    text.setFace('courier')
    text.setSize(21)
    text.draw(win)
    return button, label

def check_button(button, label, x, y):
    x1 = button.p1.getX()
    y1 = button.p1.getY()
    x1 = button.p1.getX()
    y2 = button.p1.getY()
    if x > x1 and x < x2 and y > y1 and y < y2:
        return label
    return False

def pressingofthebuttons((answer, entry, operation):
    if answer == None:
        answer = entry
        entry = 0

    else:
        if operation == '+':
            answer = add(answer, entry)
        elif operation == '-':
            answer = subtract(answer, entry)
        elif operation == '*':
            answer = multiply(answer, entry)
        elif operation == '/':
            answer = divide(answer, entry)
        elif operation == '+/-':
            answerr = change_sign(answer)
        elif operation == 'x2':
            answer = square(answer)
        elif operation == '%':
            answer = persent(answer)
        elif operation == '√':
            answer = square_root(answer)
        elif operation == '1/x':
            answer = over_x(answer)
        entry = 0
    return answer, entry

def main():
    win = GraphWin("Calculator", 300, 654)

    displayScreen = Rectangle (Point(10, 10), Point(290, 110))
    displayScreen.setFill('white')
    displayScreen.draw(win)

    buttons.append(create_button (win, 8, 115, 73, 187, "7"))
    buttons.append(create_button (win, 8, 192, 73, 264, "4"))
    buttons.append(create_button (win, 8, 269, 73, 341, "1"))
    buttons.append(create_button (win, 8, 346, 73, 418, "+/-", 'blue'))
    buttons.append(create_button (win, 8, 423, 73, 495, "x2", 'blue'))
    buttons.append(create_button (win, 8, 500, 73, 572, "MC", 'lightgreen'))
    buttons.append(create_button (win, 8, 577, 73, 649, "M+", 'lightgreen))
    buttons.append(create_button (win, 81, 115, 146, 187, "8"))
    buttons.append(create_button (win, 81, 192, 146, 264, "5"))
    buttons.append(create_button (win, 81, 269, 146, 341, "2"))
    buttons.append(create_button (win, 81, 346, 146, 418, "0"))
    buttons.append(create_button (win, 81, 423, 146, 495, "√", 'blue'))
    buttons.append(create_button (win, 81, 500, 146, 572, "M-", 'lightgreen'))
    buttons.append(create_button (win, 81, 577, 146, 649, "MR", 'lightgreen'))
    buttons.append(create_button (win, 154, 115, 219, 187, "9"))
    buttons.append(create_button (win, 154, 192, 219, 264, "6"))
    buttons.append(create_button (win, 154, 269, 219, 341, "3"))
    buttons.append(create_button (win, 154, 346, 219, 418, "."))
    buttons.append(create_button (win, 154, 423, 219, 495, "1/x", 'blue'))
    buttons.append(create_button (win, 154, 500, 219, 572, "C", 'blue'))
    buttons.append(create_button (win, 154, 577, 219, 649, "MS", 'lightgreen'))
    buttons.append(create_button (win, 227, 115, 292, 187, "/", 'blue'))
    buttons.append(create_button (win, 227, 192, 292, 264, "*", 'blue'))
    buttons.append(create_button (win, 227, 269, 292, 341, "+", 'blue'))
    buttons.append(create_button (win, 227, 346, 292, 418, "-", 'blue'))
    buttons.append(create_button (win, 227, 423, 292, 495, "%", 'blue'))
    buttons.append(create_button (win, 227, 500, 292, 572, "=", 'blue'))
    buttons.append(create_button (win, 227, 577, 292, 649, "", 'lightgreen'))


    displayString = ''
    displayTextElement = Text(Point(200, 50), "")
    displaytextElement.draw(win)
    #answer is the answer
    #entry is the number being inputed
    #operation is the function being used
    #clearNextNumber indicates a pressing of a new number will restart the operating 
    answer = None
    entry = 0
    operation = None
    clearNextNumber = False
    memory = 0
    entryString = ''

    while 1 == 1:
        clicked = win.getMouse()
        x = clicked.getX()
        y = clicked.getY()

        for b in buttons:
            button, label = b
            key = check_button(button, label, x, y)
            if key:
                if key == '=':
                    clearNextNumber = True
                    #Enter calculation to be done
                    if answer == None:
                        answer = entry
                        displayString = str(answer)
                        entry = 0
                        entryString = ''
                    else:
                        answer, entry = pressingofthebuttons(answer, entry, operation)
                        operation = None
                        displayString = '%20.3f' % (answer)
                                  
                elif key in ['+', '-', '/', '*', '%']:
                    # do the calculation
                    answer, entry = do_calculation(answer, entry, operation)
                    entryString = ''
                    operation = key
                    displayString = displayString + key
                    clearNextNumber = False
                    
                elif key == '+/-':
                    # do the calculation
                    answer, entry = do_calculation(answer, entry, operation)
                    entryString = ''
                    operation = key
                    displayString = str(answer)
                    clearNextNumber = True

                elif key == 'x2':
                    # do the calculation
                    answer, entry = do_calculation(answer, entry, operation)
                    operation = key
                    displayString = str(answer) + str('^2')
                    clearNextNumber = True

                elif key  == '√':
                    #do the calculation
                    answer, entry = do_calculation(answer, entry, operation)
                    entryString = ''
                    operation = key
                    displayString = key + str(answer)
                    clearNextNumber = True

                elif key == '1/x':
                    x = entry
                    answer, entry = do_calculation(answer, entry, operation)
                    entryString = ''
                    operation = key
                    displayString = str(answer)
                    clearNextNumber = True

                elif key == 'C':
                    # clear current text
                    displayString = ''
                    answer = None
                    entry = 0
                    entryString = ''
                    operation = None

                elif key == 'M+':
                    memory = add(float(memory), entry or answer)
                    displayString = float(memory)

                elif key == 'MR':
                    displayString = float(memory)
                    
                elif key == 'M-':
                    memory = subtract(float(memory), entry or answer)
                    displayString = float(memory)

                elif key == 'MC':
                    memory = 0

                elif key == 'MS':
                    temp = memory
                    memory = entry
                    entry = temp
                    displayString = float(memory)

                else:
                    #nuumber of keys or '.'
                    if clearNextNumber:
                        displayString = ''
                        clearNextNumber = False
                        answer = None
                        entry = 0
                        entryString = ''
                        operation = None
                    entryString = entryString + key
                    entry = float(entryString)
                    displayString = displayString + key

                displayTextElement.undraw()
                displayTextElement = Text(Point(200, 50), displayString)
                displayTextElement.setFace('courier')
                displayTextElement.setSize(21)
                displaytextElement.draw(win)

main()
                                  

                                  
                        

                                
                        
                                
    
                        

                 
                 
    
