print("Python Calculator")

first_number = ("Insert the first number: ")

if first_number.isnumeric() == False:
    print("Please insert a numeric value.")
    exit()

operation = ("Which kind of operation do you want to do? ¬ Please insert + - * / % ** only. ¬ ")

second_number = input("Insert here the second number: ")

if second_number.isnumeric() == False:
    print("Please insert a numeric value.")
    exit()

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


print("The"+ label + " of " + str(first_number) + " and " + str(second_number) + " is " + str(result))