medicine = 'Coughussin'
dosage = 5
duration = 4.5

instructions = '{} - Take {}ml by mouth every {} hours'.format(medicine, dosage, duration)
print(instructions)

instructions = '{2} - Take {1}ml by mouth every {0} hours'.format(medicine, dosage, duration)
print(instructions)

instructions = '{medicine} - Take {dosage}ml by every {duration} hours'.format(medicine = 'Sneezergen', dosage = 10, duration = 6)
print(instructions)

print("\n")

name = 'World'
message = f'Hello, {name}.'

count = 10
value = 3.14159
total = count * value
message = f'Count to {count}. Then multiply by {value}. Total is {total}'
print (message)

print ("\n")

width = 5
height = 10
message = f"Area is {width * height}, and the perimeter of this rectangle is {(2*height) + (2*width)}.\n"
print(message)
print("Or:\n")
print(f"The perimeter is {(2*height)+(2*width)}, while the area is {width * height} <unit of measurement> wide.")

print("\n")

value = 'hi'
print(f'.{value:<25}.')
print(f'.{value:>25}.')
print(f'.{value:^25}.')
print(f'.{value:-^25}.')
print(f'.{value:+^25}.')

print("\n")
