#435Write a python program that calculates the sum of the digits of a given number.
num = input("Enter Number: ")
sum = 0

for i in num:
    sum = sum + int(i)

print(sum)