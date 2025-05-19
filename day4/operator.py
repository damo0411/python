import os
import sys

my_list = ["+","-","*","/","<",">","==","!=","<=",">=","and","or"]
print ("list of operatotrs are:", my_list)

num1 = input ("Enter first number:")
num2 = input ("Enter second number:")
num1 = float (num1)
num2 = float (num2)
opr = str (input ("Enter operator:"))

def add (num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1-num2

def mul (num1, num2):
    return (num1 * num2)

def div (num1, num2):
    return (num1 / num2)

def lessthan (num1, num2):
    return (num1 < num2)

def greaterthan (num1, num2):
    return (num1 > num2)

def equal (num1, num2):
    return num1 == num2

def notequal (num1, num2):
    return num1 != num2

def lessthanorequal (num1, num2):   
    return num1 <= num2

def greaterthanorequal (num1, num2):
    return num1 >= num2

def andopr (num1, num2):
    return num1 and num2

def oropr (num1, num2):
    return num1 or num2



if opr == my_list[0]:
    print ("Addition:", add(num1,num2))
elif opr == my_list[1]:
    print ("Substraction:", sub(num1,num2))
elif opr == my_list[2]:
    print ("Multiplication:", mul(num1,num2))
elif opr == my_list[3]:
    print ("Division:", div(num1,num2)) 
elif opr == my_list[4]:
    print ("Less than:", lessthan(num1,num2))
elif opr == my_list[5]:
    print ("Greater than:", greaterthan(num1,num2))
elif opr == my_list[6]:
    print ("Equal:", equal(num1,num2))
elif opr == my_list[7]:
    print ("Not equal:", notequal(num1,num2))
elif opr == my_list[8]:
    print ("Less than or equal:", lessthanorequal(num1,num2))
elif opr == my_list[9]:
    print ("Greater than or equal:", greaterthanorequal(num1,num2))
elif opr == my_list[10]:
    print ("And operator:", andopr(num1,num2))
elif opr == my_list[11]:
    print ("Or operator:", oropr(num1,num2))
else:
    print ("Invalid operator")


