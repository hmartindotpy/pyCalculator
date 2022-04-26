import math
class Calculator:
    #call from here to move "character"
    
    def add(a,b):
        return a + b

    def subtract(a,b):
        return a - b
    
    def multiply(a,b):
        return a * b

    def factorial(a):
        return math.factorial(a)
    
    def exponent(a,b):
        return a ** b
print("Select operation.\n1. Add\n2. Subtract\n3. Multiply\n4. Factorial\n5. Exponent")
choice = input("Enter choice (1/2/3/4/5): ")
print(choice)
while True:
    
    if choice in ('1', '2', '3', '4', '5'):
        

        if choice == '1':
            num1_1 = int(input("Enter first number: "))
            num1_2 = int(input("Enter second number: "))
            print(num1_1, "+", num1_2, "=", Calculator.add(num1_1, num1_2))

        elif choice == '2':
            num2_1 = int(input("Enter first number: "))
            num2_2 = int(input("Enter second number: "))
            print(num2_1, "-", num2_2, "=", Calculator.subtract(num2_1, num2_2))

        elif choice == '3':
            num3_1 = int(input("Enter first number: "))
            num3_2 = int(input("Enter second number: "))
            print(num3_1, "*", num3_2, "=", Calculator.multiply(num3_1, num3_2))

        elif choice == '4':
            num4_1 = int(input("Enter number: "))
            print(num4_1, "!", "=", Calculator.factorial(num4_1))
        elif choice == '5':
            num3_1 = int(input("Enter number: "))
            num3_2 = int(input("Enter exponent: "))
            print(num3_1, "^", num3_2, "=", Calculator.exponent(num3_1,num3_2))
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    
    else:
        print("Invalid Input")