available_cars = [
    "toyota",
    "tesla",
    "hyundai",
    "audi",
    "porsche",
]  # list containing five cars
requested_cars = [
    "toyota",
    "honda",
    "porsche",
]  # note the odd car requested, i.e. honda
print("if Statements with Lists for multiple lists: \n")

for requested_car in requested_cars:  # loop the requested car list
    if (
        requested_car in available_cars
    ):  # check to see if each requested_car is in available_cars
        print("Displaying " + requested_car + ".")
    else:  # prints telling honda is not available
        print("Sorry, we do not have " + requested_car + ".")
print("\nFinished displaying all cars!")
