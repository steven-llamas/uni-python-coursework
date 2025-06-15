age = 25  # set the value of age to 25
print("if Statements for if-elif-else chain: ")
if age < 4:  # check whether age is < 4, price if free
    print("\nYour ticket price is $0")
    print("You are less than 4 years!")

elif age < 18:  # check whether age is < 18, price is $10
    print("\nYour ticket price is $10.")
    print("You are less than 18 years!")

else:  # if both if and elif fails, anyone above 18 is $20
    print("\nYour ticket price is $20.")
    print("Sorry, You are above 18 years!")
