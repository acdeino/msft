print("Python Calculator")

first_number = input("Insert the first number: ")

if first_number.isnumeric() == False:
    print("Please insert a numeric value.")
    exit()

operation = input("Which kind of operation do you want to do? ")

second_number = input("Insert here the second number: ")

if second_number.isnumeric() == False:
    print("Please insert a numeric value.")
    exit()

first_number = int(first_number)
second_number = int(first_number)

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
    print("Operation not recognised. ")
    exit()


print("The "+ label + " of " + str(first_number) + " and " + str(second_number) + " is " + str(result))