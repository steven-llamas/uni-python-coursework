age = 69  # set the value of age to 69
print("if Statements for multiple elif blocks: ")
if age < 4:  # check whether age is < 4, price if free
    print("\nYour ticket price is $0")
    print("You are less than 4 years!")

elif age < 18:  # check whether age is < 18, price is $10
    print("\nYour ticket price is $10.")
    print("You are above 4 years and less than 18 years!")

elif age < 65:  # check whether age is < 65, price is $20
    print("\nYour ticket price is $20.")
    print("Sorry, you are above 18 years and less than 65 years!")

else:  # if both if and elif's fails, anyone above 65 is $10
    print("\nYour ticket price is $10.")
    print("Congratulations, You are qualified for senior discount!")
