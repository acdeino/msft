import queue

colours = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'brown']
print(colours)
print(type(colours))



print("\n")

sundry = ["John", 3.14, 7, False]
print(sundry)
print(type(sundry))

my_list = []
print(my_list)
print(type(my_list))


print(f'0-based indexing into the "Colours" list ... second item: {colours[1]}')
print(f'Last item in the "Colours" List: {colours[-1]}')
print(f'Next to last item in the "Colours" list: {colours[-2]}')

print (colours[3])
#print(colours[18])

print("\nPrint a SLICE, starting at index 2 and excluding index 5: ")
print(colours[2:5])
print(type(colours[2:5]))

print("\nPrint a slice, starting at index 0 to index 3: ")
print(colours[:3])

print("\nPrint a slice, starting at index 4 to the end of the list: ")
print(colours[4:])

print("\nPrint a slice, from the fourth from the end up until the last item: ")
print(colours[-4:-1])

#Reversing and sorting the lists

colours.reverse()
print(colours)

colours.sort()
print(colours)

#Treating the list as a queue

print(colours)
color = colours.pop(0)
print("popped ", color)

print (colours)

#Add and remove elements from a list

print(colours)

colours.append("black")
colours.append("white")
print(colours)

colours.remove("yellow")
colours.remove("orange")
print(colours)

# colours.remove("whatever")

#Combine a new list with an existing list

new_colours = ["lime", "gray"]
colours.extend(new_colours)
print(colours)

#Emptying a list

colours.clear()
print(colours)

# # # # # # # # # # # # # # # # # # # # #

numbers = [1, 3, 5]

print(5 in numbers)
print(8 in numbers)

print(5 not in numbers)
print(8 not in numbers)

#FOR looping through a list:
cities = ["Chicago", "London", "Tokyo"]
for city in cities:
    print (city)

#Breaking a FOR loop in lists:

numbers = [42, 77, 16, 101, 23, 8 , 4, 15, 55]
numbers.sort()

for number in numbers:
    if number > 42: 
        break
    print(number)


print("\n")
#Use an ELSE statement:

import random
numbers = []

while len(numbers) < 5:
    numbers.append(random.randint(1,100))

for number in numbers:
    print(number)
    if number >= 90:
        print("Found at least a number greaten than 90")
        break
else:
    print("No numbers greater than 90")

print("Complete")

#Use a CONTINUE statement

values = ["laptop", 7, "phone", 3, "dslr", 5]
equipment = []

for value in values:
    if isinstance(value, str) == False:
        continue
    equipment.append(value)

print(equipment)

# Create nested FOR loops

suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

for suit in suits:
    for rank in ranks:
        print(f'{rank} of {suit}')


#Choose randomly from a list

numbers1 = [42, 77, 16, 101, 23, 8, 4, 15, 55]
selected_number1 = random.choice(numbers1)
print(selected_number1)

selected_numbers1 = random.choices(numbers1, k=3)
print(selected_numbers1)