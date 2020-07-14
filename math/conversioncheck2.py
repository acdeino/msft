first_value = input("First Number is: ")
second_value = input("Second number is: ")

if first_value.isnumeric() == False or second_value.isnumeric() == False
    print("Please Enter numbers only.")
    exit()

first_value = int(first_value)
second_value = int(second_value)

sum = first_value + second_value
print("The sum is: " + sum)