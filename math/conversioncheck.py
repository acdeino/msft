first_value = int(input("First Number is: "))
second_value = int(input("Second Number is "))

sum = first_value + second_value

print("The sum of the inserted values is: " + str(sum))

print("\n")

numeric_value_1 = "7"					
print(numeric_value_1.isnumeric())			# True
print(numeric_value_1.isalpha())            # False
print(numeric_value_1.isalnum())            # True
print(numeric_value_1.isdecimal())          # False
print(numeric_value_1.istitle())            # False
print(numeric_value_1.isupper())            # False
print(numeric_value_1.islower())            # False
print(numeric_value_1.isdigit())            # True <built-in method isdigit of str object at MemoryAddress>
print("\n")


# numeric_value_3= 7.563                    -> Integers and Floats have no isnumeric attribute. Use this attribute for strings only.
# print(numeric_value_3.isnumeric())

string_value_1 = "PorcaGaronna"
print(string_value_1.isnumeric())			# False

string_value_2 = "PorcaGaronna"
print(string_value_2.isascii())             # True
