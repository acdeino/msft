print(type("7"))
print(type(7))
print(type(7.4))
print(type('4'))
print(type(8.57848356857337436524637536786559))

print("\n")

print(isinstance("Hello", str))                                 # True
print(isinstance(7, int))                                       # True
print(isinstance(7.4, float))                                   # True
print(isinstance(7, float))                                     # False
print(isinstance(7.4, int))                                     # False
print(isinstance('4', str))                                     # True 
print(isinstance('4', int))                                     # False
print(isinstance(8.57848356857337436524637536786559, float))    # True
print(isinstance(8.57848356857337436524637536786559, int))      # False

print("\n")


print(type("7") == str)         # True
print(type("7") == int)         # False
print(type(7) == int)           # True
print(type(7) == float)         # False
print(type(7.4576) == float)    # True
print(type(7.35678) == int)     # False

print ("\n")


x = 'a literal string'
print(type(x))                  # String

y = 7
print(type(y))                  # Int

z = False
print(type(z))                  # Boolean

print("\n")


