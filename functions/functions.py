def hello():
    print("Hello")

hello()

# # # # # # # 

def say_hello():
    name = input("What's your name?  ")
    print(f'Hello {name}')


say_hello()

 # # # # # # # 

def say_hello_2(name="World"): 
    print(f"Hello, {name}")

say_hello_2()
say_hello_2("Bob")

print("\n")
# # # # # # #

def say_hello_3(greeting1 =None, name ="World"):
    if greeting1 == None:
        print(f"Hello {name}")
    else:
        print(f"{greeting1}, {name}")

say_hello_3()
say_hello_3(greeting1= "Hello")
say_hello_3("Bob")
say_hello_3("Bob", "Hello")

# # # # # # #

print(type(None))

# 
print("\n")

# # # # # # # # #

def add_two_numbers(x, y):
    return x + y

add_two_numbers(4, 6)
result = add_two_numbers(5, 7)
print(result)

print(add_two_numbers(4, 6))

print("\n")
# # # # # # # # #

def create_deck():
    suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "King", "Queen", "Ace"]
    deck = []

    for suit in suits:
        for rank in ranks:
            deck.append(f"{rank} of {suit}")

    return deck

my_deck = create_deck()
print(len(my_deck))

# # # # # # # # #

value = 1

def some_function():
    value = 10
    return value

print(value)
some_function()
print(value)

# # # # # # # # #
