print("This program allows you to do simple calculations.")
print("Sum, Difference, Product, Quotient, Module and exponent are the possible operations\n")
first_number = input("Please insert here your first number: ")

if first_number.isnumeric() == False:
    print('Please input a number.')
    exit()

operation = input("Insert here the symbol of the operation you want to do: ")

second_number = input("Insert here your second number: ")

if second_number.isnumeric() == False:
    print("Please insert a number.")
    exit()

first_number = int(first_number)
second_number = int(second_number)

result = 0
if operation == "+":
    result = first_number + second_number
    label = "sum"
elif operation == "-":
    result = first_number - second_number
    label = "difference"
elif operation == "*":
    result = first_number * second_number
    label = "product"
elif operation == "/":
    result = first_number / second_number
    label = "quotient"
elif operation == "%":
    result = first_number % second_number
    label = "modulus"
elif operation == "**":
    result = first_number ** second_number
    label = "exponential"
else:
    print("Operation not recognised.")
    exit()

print(label + " of " + str(first_number) + " " + operation + str(second_number) + " equals " + str(result))
