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
            print('Congradulations! Nice job!')
            next_question = input("Are you a fan of cows? ('y' or 'n') ")
            if next_question == "y":
                print ("Awesome! Me too!")
            else:
                print ("Oh well. Guess I don't know you as well as I thought.")
            return
        

main()
            
        
    
