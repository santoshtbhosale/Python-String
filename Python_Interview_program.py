"""
Write a program to demonstrate different number data types in Python.

a = 34
b = 34.7
c = 3 + 4j
print(type(a))
print(type(b))
print(type(c))
______________________________________________________________________________________
Write a program to create, concatenate and print a string and accessing sub-string from a given string.

s1 = input("Enter the String1:")
s2 = input("Enter the String2:")
print("First String:",s1)
print("First String:",s2)
s = s1 + s2
print("Concatenate of Two String:",s)
print("Sub-String from the given string is:",s[1:5])
______________________________________________________________________________________
Write a python script to print the current date in the following format “Sun May 29 02:26:23 IST 2017”

import time
d = time.localtime()
print(time.strftime("%a %b %d %H:%M:%S %Z %Y",d))
____________________________________________________________________________________
Write Star Patteren

n = 5
for i in range(n):
    for j in range(i):
        print('*',end=" ")
    print()
for i in range(n,0,-1):
    for j in range(i):
        print('*',end=" ")
    print()
______________________________________________________________________________________
Write a Python script that prints prime numbers less than 20.

for num in range(1,21):
    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                break
        else:
            print(num)
_______________________________________________________________________________________
Write a python program to find factorial of a number using Recursion.

def factorial(n):
    if n == 0:
        result = 1
    else:
        result = n*factorial(n-1)
    return result
num = int(input("Enter the Number:"))
print(factorial(num))
___________________________________________________________________________________
Write a program that accepts the lengths of three sides of a triangle as inputs.
The program output should indicate whether or not the triangle is a right triangle (Recall from
the Pythagorean Theorem that in a right triangle, the square of one side equals
the sum of the squares of the other two sides).

base = float(input("Enter the Base:"))
per = float(input("Enter the Per:"))
hypo = float(input("Enter the hypo:"))
if hypo ** 2 == base ** 2 + per ** 2:
    print("The Traingle is Right Traingle")
else:
    print("The Traingle is not Right Traingle")
____________________________________________________________________________________________________
Write a Python class to implement pow (x, n)

def pow(x, y):
    if y == 0:
        return 1
    elif (int(y%2) == 0):
        return pow(x, int(y/2)) * pow(x, int(y/2))
    else:
        return (x * pow(x, int(y/2)) * pow(x, int(y/2)))
x = 3
y = 2
print(pow(x, y))
__________________________________________________________________
Write a Python class to reverse a string word by word.

class Reverse():
    def reverse_word(self,s):
        return ''.join(reversed(s.split()))
print(Reverse().reverse_word('Welcome to python'))
__________________________________________________________________
Python Program for Find remainder of array multiplication divided by n
"""



