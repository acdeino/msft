print("Capitalising")
message = str.capitalize('first message')
print(message)

message = 'second message'.capitalize()
print(message)

message = "third message"
print(message.capitalize())

print('\n')

message = "hello world"
print(message.lower())
print(message.upper())

message  = message.title()
print(message)
print(message.swapcase())

print("\n")
print("- Letters count -")
location = 'Mississippi'
print(location.count('s'))
print(location.count('p'))

print("\n")
print("- String character count -")
print(len('How many letters in this string?'))
print(len("Llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch"))

print("\n")
print("- String Start/End characters -")
message = 'racecar'
print(message.startswith('r'))
print(message.startswith("a"))
print(message.startswith('ra'))

print(message.startswith('r'))
print(message.startswith("a"))
print(message.endswith("ar"))

print("\n")
print("- Find Words -")
message = 'The quick brown fox jumps over the lazy dog'
print(message.find('q'))
print(message.find('t'))
print(message.find("T"))
print(message.find("H"))

print("\n")

print("- Strip Management, Left/Right/Centre -")
message = ' middle  '
print('.' + message.lstrip() + ".")
print("." + message.rstrip() + ".")
print("." + message.strip() + ".")

print("\n")

print("- Word exchange -")
message = "brevity is the essence of the wit"
message = message.replace("essence", 'soul')
print(message)

print("\n")
print("- Hypens Adjusting -")
message = "howdy"
print(message.rjust(20))
print(message.rjust(20, '-'))
print(message.ljust(20))
print(message.ljust(20, "-"))

print("\n")
