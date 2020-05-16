import datetime

print("Today's date?\n")
date = datetime.datetime.now()
dateday = input()
print(dateday)
print(date, "\n")



print("How many calories did you eat for breakfast?\n")
breakfastcalories = int(input())

print("How many calories did you eat for lunch?\n")
lunchcalories = int(input())

print("How many calories did you eat for dinner?\n")
dinnercalories =  int(input())


print("How many calories did you eat today?\n")
totalcalories = breakfastcalories + lunchcalories + dinnercalories
print("Calorie content for "+ dateday + " is " + str(totalcalories))

