history = []

def calculate(a, b, op):
    if op == "+":
       return a + b
    elif op == "-":
         return a - b
    elif op == "*":
         return a * b
    elif op == "/":
         return a / b
    else:
        return "Invalid operation"

while True:
     num1 = float(input("Enter first number: "))
     num2 = float(input("Enter second number: "))
     operator = input("Enter operator (+, -, *, /):")

     result = calculate(num1, num2, operator)
     print ("Result:", result)
     history.append(result)

     cont = input("Do you want to continue? (yes to continue): ").lower()
         
print("Calculation History:", history)

