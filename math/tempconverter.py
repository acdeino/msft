# Temperature converter from fahrenheit to celsius converter

print("This program will convert into Celsius(°C) the inserted Fahrenheit(°F) temperature\n")
fahrenheit = (input("What's the temperature in Fahrenheit(°F)? "))      # Gets the input value as Fahrenheit(°F) degrees

if fahrenheit.isnumeric() == False:                                     # Checks if the input value is numeric. If it is, it computes, otherwise returns an error message
    print ("The Input is not a number, try again.")
    exit()

fahrenheit = int(fahrenheit)


celsius = int((fahrenheit - 32) * 5/9)                                  # Computes the Celsius value from the fahrenheit

print("The Celsius(°C) temperature is: " + str(celsius))                            # Prints the Celsius value