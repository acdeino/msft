print("This program allows you to do simple calculations.")
print("Sum, Difference, Product, Quotient, Module and exponent are the possible operations\n")
first_value = input("Please insert here your first number: ")

if first_value.isnumeric() == False:
    print("Please insert a numerical value.")
    exit()

operation = ("Insert here the symbol of the operation you want to do: ")

second_value = ("Insert here your second number: ")

if second_value.isnumeric() == False:
    print("Please insert a numerical value.")
    exit()

first_value = int(first_value)
second_value = int(second_value)

result = 0
if operation == "+":
    result = first_value + second_value
    label = "sum"
elif operation == "-":
    result = first_value - second_value
    label = "difference"
elif operation == "*":
    result = first_value * second_value
    label = "product"
elif operation == "/":
    result = first_value / second_value
    label = "quotient"
elif operation == "%":
    result = first_value % second_value
    label = "modulus"
elif operation == "**":
    result = first_value ** second_value
    label = "exponential"
else:
    print("Operation not recognised.")
    exit()

print(label + " of " + str(first_value) + " " + operation + str(second_value) + " equals " + str(result))