#Introduction to Programming
#Jennifer Gunther
#26 February 2018

animal = "cow"

def main():
    print ("Guess what animal I am thinking of.")
    guess = input("What animal am I thinking of?" '')
    correct = False
    while not correct:
        if guess == 'q':
            quit(0)
        elif guess != 'cow':
            print("Sorry! Try Again.")
            guess = input("What animal am I thinking of?" '')
            guess = guess.lower()

        else:
            print('Congradulations!')
            return
        

main()
            
        
    
