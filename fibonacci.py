# Intorduction to Programming
# Jennifer Gunther
# 4 February 2018

print ("The purpose of this program is to write a Fibonacci sequence")

def fib(n):
    a,b = 1,1
    for i in range(n-1):
        a,b = b, a+b
    return a

def main():
    n = int(input("Enter the Fibonacci term "))
    print (fib(n))

main()

    

