#CMPT 120 - Lab 6
# Jennifer Gunther
# 22 March 2018

def showIntro():
    print("Welcome to the Arthmetic Engine!")
    print("=================================\n")
    print("Valid commands are 'add', 'mult', 'sub', 'div', and 'quit'.\n")

def showOutro():
    print("\nThank you for using the Arithmetic Engine...")
    print("\nPlease come back again soon!")

def doLoop():
    while True:
        cmd = input("What computation do you want to perform? ")
        cmd = cmd.lower()
        duck = False
        while duck==False:
            if cmd == "add" or cmd == "sub" or cmd == "mult" or cmd == "div" or cmd == "quit":
                duck = True
            else:
                print(cmd + " is not a valid command.")
                cmd = input("What computation do you want to perform? ")
                cmd = cmd.lower()
        if cmd == "quit":
            break

        try:
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
        except:
            print("That input is not valid. Please enter a number")
        if num2 == 0:
            raise Exception("Unable to divide by zero!")
            continue
        if cmd == "add":
            result = num1 + num2
        elif cmd == "sub":
            result = num1 - num2
        elif cmd == "mult":
            result = num1 * num2
        elif cmd == "div":
            result = num1 // num2
       
 # will crash because of division by zero
        print("The result is " + str(result) + ".\n")

def main():
          showIntro()
          doLoop()
          showOutro()

main()
