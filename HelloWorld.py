# print("Hello World!")
# name = input("What is your name? ")
# print ("I hope you're enjoying yourself " + name)
# age = 2023 - int(input("What is your birth year, " + name + " "))
# print ("You are now " + str(age) + " years old")

# if age > 40:
#    print("You are old, " + response)
# elif age > 30:
#     print("You are in your prime time, " + name)
#else:
#     print("You are young!")

response = "y"
while response == "y":
    weight = float(input("Weight: "))
    units = input("(K)g or (L)bs: ")
    if units.lower()=="l":
        print("Weight in Kg: " + str(weight / 2.205))
    elif units.lower()=="k":
        print("Weight in lbs: " + str(weight * 2.205))
    else:
        print("I'm not sure I can help!")
    response = input("Do you want to try with another weight (y/n)? ")
