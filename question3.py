#Write a python program that calculates the factorial of a given number.
num = int(input("Enter the number "))
fact = 1
if (num == 0):
    print (" The factorial of 0 is ", 1)
elif (num < 0):
    print ("Factorial not defined for given number ")
else :
    while (num > 0) :
        fact = num * fact
        num = num - 1
    print ("Factorial of the given number is ",fact)