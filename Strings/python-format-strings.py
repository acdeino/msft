first_string = 'Hello'
second_string = "Hello"

print(first_string == second_string)

print("\n")

third_string = 'A single quoted literal string with a " (double) quote'
fourth_string = "A double quoted literal string with a '(single) quote"

print(third_string)
print(fourth_string)
print(third_string == fourth_string)

print("\n")

fifth_string = 'A single quoted literal string with an \' escaped single quote'
sixth_string = "A double quoted literal string with an \' escaped double quote"
seventh_string = 'A literal string with a \n new line character'
eighth_string = "A literal string with a \t tab character"

print(fifth_string)
print(sixth_string)
print(seventh_string)
print(eighth_string)

print("\n")

nineth_string = r"A literal string with a \n line character print raw"

print(nineth_string)

print("\n")

tenth_string = ''' A literal string
or more than one line,
sometimes known as verbatim string - using single quotes'''
eleventh_string = """Another literal fifth_string
    on more than one line,
using double quotes"""

print(tenth_string, "\n")
print(eleventh_string)

print("\n")

first_name = 'Conrad'
second_name = 'Grant'
third_name = 'Bob'

print(first_name, second_name)
print(first_name + second_name, third_name)
print(first_name, second_name, third_name)
print(first_name, second_name, third_name, sep=" - ")
print(first_name, second_name, third_name, sep=" - ", end=".")

print("\n")
