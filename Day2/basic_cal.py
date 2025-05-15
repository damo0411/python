def addition (num1, num2):
    return num1 + num2

def sub(num1,num2):
    return num1-num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    if (num2 == 0):
        return "Error! Division of by Zero"
    else:
        return num1/num2
    
addition(10,2)
sub(10,2)
mul(10,2)
div(10,2)

print("Addition of 10 and 2 is: ", addition(10,2))
print("Subtraction of 10 and 2 is: ", sub(10,2))        
print("Multiplication of 10 and 2 is: ", mul(10,2))
print("Division of 10 and 2 is: ", div(10,2))



