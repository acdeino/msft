
# Values Declarations
first_value = 5
second_value = 4

# Math Operations
sum = first_value + second_value
difference = first_value - second_value
product = first_value * second_value
quotient = first_value / second_value
modulus = first_value % second_value
exponent = first_value ** second_value

# Printing the results, after converting the Int data into Strings
print("Sum is: " + str(sum))
print("Difference is: " + str(difference))
print("Product is: " + str(product))
print("Quotient is: " + str(quotient))
print("Modulus is: " + str(modulus))
print("Exponent is: " + str(exponent))


# Python uses the PEMDAS approach (Parentheses-Exponents-Multiplications-Division-Addition-Subtraction)

    # Parentheses
print(3 + 4 * 5)    # = 23
  # that is not the same as
print((3+4) * 5)    # = 35

    # Division
print(type(quotient))
print(quotient)
# Convert Quotient value in an Str and then print it
print("The converted (into a string) Quotient value is: " + str(quotient))


# Checking the type of a float and then convert it into an integer
pi = 3.14159
print(type(pi))
print(int(pi))

uptime = 99.99
print(type(uptime))
print(int(uptime))
  
 # To avoid truncation, we can use the round() function
pi = 3.14159
print(type(pi))
print(int(pi))
print("The converted value of Pi into Int is: " + str(pi))
print(round(pi))


uptime = 99.99
print(type(uptime))
print(int(uptime))
print("The converted value of Uptime into Int is: " + str(uptime))
print(round(uptime))

    # To better understand how the round() function works, here are two examples
# These are some values
third_value = 7.654321
fourth_value = 9.87654

# We're now gonna round to the 3rd decimal figure and then print them
print(round(third_value, 3))
print(round(fourth_value, 3))

# Another way to do that is to declare the round function directly from the variable declaration like this
fifth_value = round(7.654321, 2)
sixth_value = round(9.87654, 3)

print(fifth_value)
print(sixth_value)
