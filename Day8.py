print("Calculate")

def cal(n1,n2,op):
    if op == "+":
        return n1 + n2
    elif op == "-":
        return n1 - n2
    elif op == "*":
        return n1 * n2
    elif op == "/":
        if b == 0:
            return "Error: Can't divide by zero"
        return n1 / n2
    return ("error")

a = int(input("Enter Number 1: "))
b = int(input("Enter Number 2: "))
c = input("Operator: ")

result = cal(a,b,c)
print(result)



print("Grade Checker")

def marks(n):
    if n < 0 or n > 100:
        print("Error: Mark must be between 0 and 100")
    if n < 35:
        return "Fail"
    elif n < 55:
        return "Pass"
    elif n < 75:
        return "Merit"
    return "Distinction"

Sl = int(input("Enter the Mark: "))
print(marks(Sl))
    


