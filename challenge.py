
value = input ("Would you like to continue? ")

if value == "y" or value == "yes" or value == "Y" or value == "Yes":
    print("Processing...\n")
    print("Completed!")
elif value == "n" or value == "no" or value == "N" or value == "No":
    print("Goodbye!")
else:
    print("Try Again!")
