#Jennifer Gunther
#Project 5
#classes

from graphics import *
from calc_functions import *
from try2_newcalculator import Calculator

class Button:

    """A button is a labeled rectangle in a window.
    It is activated or deactivated with the activate()
    and deactivate() methods. The clicked(p) method
    returns true if the button is active and p is inside it."""

    def __init__(self, win, center, width, height, label, color = 'aquamarine'):
        """ Creates a rectangular button, eg:
        qb = Button(myWin, centerPoint, width, height, 'Quit') """ 

        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill(color)
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.label.setSize(20)

    def clicked(self, p):
        "Returns true if button active and p is inside"
        return (self.xmin <= p.getX() <= self.xmax and
                self.ymin <= p.getY() <= self.ymax)

    def getLabel(self):
        "Returns the label string of this button."
        return self.label.getText()

class Display:

    """The display is the overall display rectangle and it includes
    one or more text elements (lines)."""

    def __init__(self, win, center, width, height, color = 'lightcyan'):
        # initialize screen and draw it
        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.screen = Rectangle(p1,p2)
        self.screen.setFill(color)
        self.screen.draw(win)
        self.win = win

        # initialize text elements (empty to start)
        self.textElems = []
        self.corners = []

    def addLine(self, corner, text=''):
        # create text element, draw it, and store in list
        displayTextElement = Text(corner, text)
        displayTextElement.setFace('arial')
        displayTextElement.setSize(20)
        displayTextElement.draw(self.win)
        self.textElems.append(displayTextElement)
        self.corners.append(corner)

    def setLine(self, line, text):
        # set new text on specific display line (0, 1, 2...)
        # undraw old one first
        self.textElems[line].undraw()

        # then create new one and save it
        displayTextElement = Text(self.corners[line], text)
        displayTextElement.setFace('arial')
        displayTextElement.setSize(20)
        displayTextElement.draw(self.win)
        self.textElems[line] = displayTextElement

class Calculator:
    def __init__(self):
        self.buttons = []


    def do_calculation(self, answer, entry, operation):
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
                answer = change_sign(answer)
            elif operation == 'x2':
                answer = square(answer)
            elif operation == '%':
                answer = percent(answer)
            elif operation == '√':
                answer = square_root(answer)
            elif operation == '1/x':
                answer = over_x(answer)
            elif operation == 'sin':
                answer = sine(answer)
            elif operation == 'cos':
                answer = cosine(answer)
            elif operation == 'tan':
                answer = tangent(answer)
            elif operation == '10^x':
                answer = power_of_ten(answer)
            elif operation == 'log':
                answer = log_button(answer)
            elif operation == 'ln':
                answer = natural_log(answer)
            elif operation == 'sin^-1':
                answer = arc_sin(answer)
            elif operation == 'cos^-1':
                answer = arc_cos(answer)
            elif operation == 'tan^-1':
                answer = arc_tan(answer)
            elif operation == 'x^y':
                answer = x_to_the_y(answer, entry)
            entry = 0
        return answer, entry

    def create_window(self, scientific_mode):
        if scientific_mode:
                
            win = GraphWin("Calculator", 446, 654)
            display = Display(win, Point(223, 60), 426, 100)


            del self.buttons[:]
            self.buttons.append(Button(win, Point(40.5, 151), 65, 72, "7"))
            self.buttons.append(Button(win, Point(40.5, 228), 65, 72, "4"))
            self.buttons.append(Button(win, Point(40.5, 305), 65, 72, "1"))
            self.buttons.append(Button(win, Point(40.5, 382), 65, 72, "+/-", 'blue'))
            self.buttons.append(Button(win, Point(40.5, 459), 65, 72, "x2", 'blue'))
            self.buttons.append(Button(win, Point(40.5, 536), 65, 72, "(", 'blue'))
            self.buttons.append(Button(win, Point(40.5, 613), 65, 72, "M+", 'lightskyblue'))
            self.buttons.append(Button(win, Point(113.5, 151), 65, 72, "8"))
            self.buttons.append(Button(win, Point(113.5, 228), 65, 72, "5"))
            self.buttons.append(Button(win, Point(113.5, 305), 65, 72, "2"))
            self.buttons.append(Button(win, Point(113.5, 382), 65, 72, "0"))
            self.buttons.append(Button(win, Point(113.5, 459), 65, 72, "√", 'blue'))
            self.buttons.append(Button(win, Point(113.5, 536), 65, 72, ")", 'blue'))
            self.buttons.append(Button(win, Point(113.5, 613), 65, 72, "MR", 'lightskyblue'))
            self.buttons.append(Button(win, Point(186.5, 151), 65, 72, "9"))
            self.buttons.append(Button(win, Point(186.5, 228), 65, 72, "6"))
            self.buttons.append(Button(win, Point(186.5, 305), 65, 72, "3"))
            self.buttons.append(Button(win, Point(186.5, 382), 65, 72, "."))
            self.buttons.append(Button(win, Point(186.5, 459), 65, 72, "1/x", 'blue'))
            self.buttons.append(Button(win, Point(186.5, 536), 65, 72, "C", 'blue'))
            self.buttons.append(Button(win, Point(186.5, 613), 65, 72, "MS", 'lightskyblue'))
            self.buttons.append(Button(win, Point(259.5, 151), 65, 72, "/", 'blue'))
            self.buttons.append(Button(win, Point(259.5, 228), 65, 72, "*", 'blue'))
            self.buttons.append(Button(win, Point(259.5, 305), 65, 72, "+", 'blue'))
            self.buttons.append(Button(win, Point(259.5, 382), 65, 72, "-", 'blue'))
            self.buttons.append(Button(win, Point(259.5, 459), 65, 72, "%", 'blue'))
            self.buttons.append(Button(win, Point(259.5, 536), 65, 72, "=", 'blue'))
            self.buttons.append(Button(win, Point(259.5, 613), 65, 72, "M-", 'lightskyblue'))       
            self.buttons.append(Button(win, Point(332.5, 151), 65, 72, "sin", 'blue'))
            self.buttons.append(Button(win, Point(332.5, 228), 65, 72, "cos", 'blue'))
            self.buttons.append(Button(win, Point(332.5, 305), 65, 72, "tan", 'blue'))
            self.buttons.append(Button(win, Point(332.5, 382), 65, 72, "10^x", 'blue'))
            self.buttons.append(Button(win, Point(332.5, 459), 65, 72, "log", 'blue'))
            self.buttons.append(Button(win, Point(332.5, 536), 65, 72, "ln", 'blue'))
            self.buttons.append(Button(win, Point(332.5, 613), 65, 72, "MC", 'lightskyblue'))
            self.buttons.append(Button(win, Point(405.5, 305), 65, 72, "sin^-1", 'blue'))
            self.buttons.append(Button(win, Point(405.5, 382), 65, 72, "cos^-1", 'blue'))
            self.buttons.append(Button(win, Point(405.5, 459), 65, 72, "tan^-1", 'blue'))
            self.buttons.append(Button(win, Point(405.5, 536), 65, 72, "x^y", 'blue'))
            self.buttons.append(Button(win, Point(405.5, 613), 65, 72, "Sci", 'lightskyblue'))


        else:
            win = GraphWin("Calculator", 373, 654)

            display = Display(win, Point(183, 60), 353, 100)

            del self.buttons[:]
        
            self.buttons.append(Button(win, Point(40.5, 151), 65, 72, "7"))
            self.buttons.append(Button(win, Point(40.5, 228), 65, 72, "4"))
            self.buttons.append(Button(win, Point(40.5, 305), 65, 72, "1"))
            self.buttons.append(Button(win, Point(40.5, 382), 65, 72, "+/-", 'blue'))
            self.buttons.append(Button(win, Point(40.5, 459), 65, 72, "x2", 'blue'))
            self.buttons.append(Button(win, Point(40.5, 536), 65, 72, "MC", 'blue'))
            self.buttons.append(Button(win, Point(40.5, 613), 65, 72, "M+", 'lightskyblue'))
            self.buttons.append(Button(win, Point(113.5, 151), 65, 72, "8"))
            self.buttons.append(Button(win, Point(113.5, 228), 65, 72, "5"))
            self.buttons.append(Button(win, Point(113.5, 305), 65, 72, "2"))
            self.buttons.append(Button(win, Point(113.5, 382), 65, 72, "0"))
            self.buttons.append(Button(win, Point(113.5, 459), 65, 72, "√", 'blue'))
            self.buttons.append(Button(win, Point(113.5, 536), 65, 72, "M-", 'blue'))
            self.buttons.append(Button(win, Point(113.5, 613), 65, 72, "MR", 'lightskyblue'))
            self.buttons.append(Button(win, Point(186.5, 151), 65, 72, "9"))
            self.buttons.append(Button(win, Point(186.5, 228), 65, 72, "6"))
            self.buttons.append(Button(win, Point(186.5, 305), 65, 72, "3"))
            self.buttons.append(Button(win, Point(186.5, 382), 65, 72, "."))
            self.buttons.append(Button(win, Point(186.5, 459), 65, 72, "1/x", 'blue'))
            self.buttons.append(Button(win, Point(186.5, 536), 65, 72, "C", 'blue'))
            self.buttons.append(Button(win, Point(186.5, 613), 65, 72, "MS", 'lightskyblue'))
            self.buttons.append(Button(win, Point(259.5, 151), 65, 72, "/", 'blue'))
            self.buttons.append(Button(win, Point(259.5, 228), 65, 72, "*", 'blue'))
            self.buttons.append(Button(win, Point(259.5, 305), 65, 72, "+", 'blue'))
            self.buttons.append(Button(win, Point(259.5, 382), 65, 72, "-", 'blue'))
            self.buttons.append(Button(win, Point(259.5, 459), 65, 72, "%", 'blue'))
            self.buttons.append(Button(win, Point(259.5, 536), 65, 72, "=", 'blue'))
            self.buttons.append(Button(win, Point(259.5, 613), 65, 72, "Sci", 'lightskyblue'))       
            self.buttons.append(Button(win, Point(332.5, 151), 65, 72, "(", 'blue'))
            self.buttons.append(Button(win, Point(332.5, 228), 65, 72, ")", 'blue'))

        # add display lines 1&2, empty for now
        display.addLine(Point(275, 50))
        display.addLine(Point(275, 75))
        display.setLine(0, '')
        display.setLine(1, '')

        return win, display

    def run(self):
        scientific_mode = False
        win, display = self.create_window (scientific_mode)
        #answer is running total
        #entry is the current number being typed in
        #operation is adding the math funtion to the equals display
        #clearNextNumber means the display should be cleared next time a number is pressed
        answer = None
        entry = 0
        operation = None
        clearNextNumber = False
        memory = 0
        entryString = ''
        displayString1 = ''
        displayString2 = ''
        
        while 1 == 1:
            clicked = win.getMouse()
            x = clicked.getX()
            y = clicked.getY()

            for b in self.buttons:
                if b.clicked(Point(x,y)):
                    key = b.getLabel()
                    if key == '=':
                        clearNextNumber = False
                        if answer == None:
                            answer = entry
                            displayString1 = ''
                            displayString2 = str(answer)
                            entry = 0
                            entryString = ''
                        else:
                            answer, entry = self.do_calculation(answer, entry, operation)
                            operation = None
                            displayString1 = ''
                            displayString2 = '%20.3f' % (answer) 

                    elif key in ['+', '-', '/', '*', '%']:
                        answer, entry = self.do_calculation(answer, entry, operation)
                        entryString = ''
                        operation = key
                        displayString1 = displayString1 + key
                        displayString2 = str(answer)
                        clearNextNumber = False
                        
                    elif key == '+/-':
                        answer, entry = self.do_calculation(answer, entry, operation)
                        operation = key
                        displayString1 = ''
                        displayString2 = str(answer)
                        clearNextNumber = True

                    elif key == 'x2':
                        answer, entry = self.do_calculation(answer, entry, operation)
                        operation = key
                        displayString1 = str(answer) + str('^2')
                        displayString2 = ''
                        clearNextNumber = True

                    elif key  == '√':
                        answer, entry = self.do_calculation(answer, entry, operation)
                        entryString = ''
                        operation = key
                        displayString1 = key + str(answer)
                        displayString2 = str(answer)
                        clearNextNumber = True

                    elif key == '1/x':
                        x = entry
                        answer, entry = self.do_calculation(answer, entry, operation)
                        entryString = ''
                        operation = key
                        displayString1 = '1/' + str(answer)
                        displayString2 = str(answer)
                        clearNextNumber = True

                    elif key == 'C':
                        # clear current text
                        displayString1 = ''
                        displayString2 = ''
                        answer = None
                        entry = 0
                        entryString = ''
                        operation = None

                    elif key == 'M+':
                        memory = add(float(memory), entry or answer)
                        displayString1 = ''
                        displayString2 = str(memory)

                    elif key == 'MR':
                        displayString1 = ''
                        displayString2 = str(memory)
                        
                    elif key == 'M-':
                        memory = subtract(float(memory), entry or answer)
                        displayString1 = ''
                        displayString2 = str(memory)

                    elif key == 'MC':
                        memory = 0

                    elif key == 'MS':
                        temp = memory
                        memory = entry
                        entry = temp
                        displayString1 = ''
                        displayString2 = str(memory)
                        
                    elif key == '10^x':
                        answer, entry = self.do_calculation(answer, entry, operation)
                        operation = key
                        displayString1 = '10^' + str(answer)
                        displayString2 = ''
                        clearNextNumber = True
                        
                    elif key in ['sin', 'cos', 'tan', 'log', 'ln', 'sin^-1', 'cos^-1', 'tan^-1']:
                        answer, entry = self.do_calculation(answer, entry, operation)
                        operation = key

                        if answer == None:
                            answer = entry
                            displayString1 = key + '(' + entryString + ')'
                            displayString2 = str(answer)
                            entry = 0
                            entryString = ''
                        else:
                            answer, entry = self.do_calculation(answer, entry, operation)
                            operation = None
                            displayString1 = key + '(' + entryString + ')'
                            displayString2 = '%20.3f' % (answer)

                        clearNextNumber = True


                    elif key == 'x^y':
                        answer, entry = self.do_calculation(answer, entry, operation)
                        entryString = ''
                        operation = key
                        displayString1 = displayString1 + '^'
                        displayString2 = str(answer)
                        clearNextNumber = False

                    elif key == 'Sci':
                        #kill old window; invert it; create new one; reset
                        win.close()
                        scientific_mode = not scientific_mode
                        win, display = self.create_window (scientific_mode)
                        displayString1 = ''
                        displayString2 = ''
                        clearNextNumber = False
                        answer = None
                        entry = 0
                        entryString = ''
                        operation = None

                    elif key == '(':
                        entryString = ''
                        displayString1 = displayString1 + '(' + entryString
                        if answer:
                            displayString2 = str(answer)
                        else:
                            displayString2 = ''
                        clearNextNumber = False

                    elif key == ')':
                        displayString1 = displayString1 + ')'
                        if answer:
                            displayString2 = str(answer)
                        else:
                            displayString2 = ''
                        clearNextNumer = False

                        
                    else:
                        # number keys or '.'
                        if clearNextNumber:
                            displayString1 = ''
                            displayString2 = ''
                            clearNextNumber = False
                            answer = None
                            entry = 0
                            entryString = ''
                            operation = None
                        entryString = entryString + key
                        if entryString[0] == '.':
                            entry = eval("0" + entryString)
                        else:
                            entry = eval(entryString) 
                        displayString1 = displayString1 + key
                        displayString2 = key

                    # update both display lines
                    display.setLine(0, displayString1)
                    display.setLine(1, displayString2)

myCalc = Calculator()
myCalc.run()

