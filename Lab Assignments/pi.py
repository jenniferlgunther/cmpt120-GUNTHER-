# Introduction to Programming
# Jennifer Gunther
# 4 February 2018

print ("This function is going to find the approximate value of pi.")

def main():
    n = int(input("Enter the number of the terms to use "))
    pi = 0
    sign = 1
    for i in range (1, n * 2 + 1, 2):
        term = 4 / i * sign
        pi = pi + term
        sign = sign * - 1
    print ("The aproximate value of pi is", pi)

main()

    
