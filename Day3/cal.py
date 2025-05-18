import sys
import os

num1 = float (sys.argv[1])
num2 = float (sys.argv[3])
opr = str (sys.argv[2])

def add (num1, num2):
    return num1 + num2

def sub(num1,num2):
    return num1 - num2

def mul (num1, num2):
    return (num1 * num2)

if opr == "+":
    print ("Addition:", add(num1,num2))
elif opr == "-":
    print ("substraction:", sub(num1,num2))
elif opr == "*":
    print ("multiplication:", mul(num1,num2))
else:
    print ("Invalid operator")

# # This code is a simple calculator that takes two numbers and an operator as command line arguments.
# # It performs addition, subtraction, or multiplication based on the operator provided.

print (os.getenv("password"))
