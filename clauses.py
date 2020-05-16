
print("Insert a number: \n")
value = input()

if value == "7":
    print("Value is 7")
elif value == "8":
    print("Value is 8")
elif value > "10":
    print("Value is bigger or equal to 10")
elif value < "10":
    print("Value is smaller than 10")
elif value != "7":
    print("Value is not 7")
else:
     print ("Hello")


first_value = True
second_value = "6"
if first_value:
    if second_value == "6":
        print("Ok!")

print("\n")


print(type("Hello World!"))
print(type(7))
print(type(18.456))

print(type(True))    
print(type(False))

print(type('True'))
print(type('False'))
print("\n")



print(bool("True"))
print(bool("False"))
print(bool(" "))
print(bool(' '))
print(bool("String"))
print("\n")

print(bool(7))
print(bool(0))
print(bool(-1))
print(bool(1.58))
print(bool(-1.58))
print("\n")

print(1 + 1 == 3)
print(2 + 2 == 4)

print(3 == 4)
print(3 != 4)
print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
print("\n")

first_number = 5
second_number = 0
true_value = True
false_value = False

if first_number > 1 and first_number < 10:
    print("The Number is between 1 and 10.")
if first_number > 1 or second_number < 1:
    print("At least one value is greater than one")

print(not true_value)
print(not false_value)

if not first_number > 1 and second_number < 10:
    print("Both values passe the test")
else:
    print("Both values do NOT pass the test")

print("\n")


print ("Finished!")