cars = ["toyota", "tesla", "hyundai", "audi", "porsche"]  # list containing five cars
print("if Statements with Lists for checking special items: \n")

for car in cars:
    if car == "audi":  # check if the car is audi
        print("Sorry, we are out of AUDI cars right now.")
    else:  # display all other cars
        print("Displaying " + car + ".")
print("\nFinished displaying all cars!")
