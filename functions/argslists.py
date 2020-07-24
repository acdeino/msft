

def print_args(*args):
    for arg in args:
        print(f"Arg in {arg}")
    

print_args("a")
print_args("a", "b")
print_args("a", "b", "c")


print("\n")
# # # # # # # # # #

def print_args_2(*args):
    print(args)
    print(type(args))

print_args_2("a")
print_args_2("a","b")
print_args_2("a","b","c")


print("\n")
# # # # # # # # # # #

def print_keyword_args(**kwargs):
    third = kwargs.get('third', None)
    if third != None:
        print ("third argument is: ", third)

print_keyword_args(first = 'a')
print_keyword_args(first = "a", second = 'b')
print_keyword_args(first = 'a', second = 'b', third = 'c')



print("\n")
# # # # # # # # # # # # 

def print_keyword_args_2(**kwargs):
    print(kwargs)
    print(type(kwargs))

    for key, value in kwargs.items():
        print(f'{key} = {value}')
    
    third = kwargs.get('third', None)
    if third != None:
        print('Third arg')