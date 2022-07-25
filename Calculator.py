num1 = input("please insert your first number ")
num2 = input("please insert your second number ")
operation = input("Please insert your desired operation among: +, -, *, /: ")
if operation == "+":
    result = float(num1) + float(num2)
elif operation == "-":
    result = float(num1) - float(num2)
elif operation == "*":
    result = float(num1) * float(num2)
elif operation == "/":
    result = float(num1) / float(num2)
else:
    result = "The operation is not valid"

print(result)
