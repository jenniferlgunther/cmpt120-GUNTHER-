# CMPT 120 Intro to Programming
# Lab #5 – Working with Strings and Functions
# Author: Jennifer Gunther
# Created: 2018-02-22

# JA: You have a single commit to the repository. It you commit after
# each step, it is possible to track the changes to the file

#Get the user's first and last name
def nameDetails():
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    return first, last

#Configure Marist Style email
def maristStyle(first, last):
    uname = first + "." + last
    return uname.lower()

#Check password strength
def passwordCheckStrength (passwd):
    if len(passwd) >=8 and passwd!=passwd.lower():
        return True
    else:
        return False

def passwordCheckLength (uname):
    passwd = input("Create a new password: ")
    while not passwordCheckStrength(passwd):
        print("That password is feeble! It must contain 8 characters and at least one Uppercase!")
        passwd = input("Create a new password: ")
    return passwd

def main():
    first, last = nameDetails()
    uname = maristStyle(first, last) 
    passwd = passwordCheckLength(uname)
    print("The force is strong in this one…")
    print("Account configured. Your new email address is", uname + "@marist.edu")
    
main()
