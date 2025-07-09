#Simple Calculator
a=float(input("Enter first number: "))
b=float(input("Enter second number: "))

print("+ for Addition")
print("- for Subtraction")
print("* for Multiplication")
print("/ for Division")

operation=input("Enter operation: ")
if operation == '+':
    print("Result:",a+b)
elif operation == '-':
    print("Result:",a-b)
elif operation =='*':
    print("Result:",a*b)
else:
    print("Invalid operation Found")
          
