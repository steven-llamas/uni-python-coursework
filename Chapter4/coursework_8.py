# cars = ['toyota', 'tesla', 'hyundai', 'audi', 'porsche']    # list containing five cars
cars = []  # emplty list of cars
print("if Statements with Lists for checking that a list is not empty: \n")

if cars:  # quick check, Python returns True if the list conatins at least one item
    for car in cars:
        print("Displaying " + car + ".")
    print("\nFinished displaying all cars!")
else:  # empty list evaluates to False
    print("Sorry, no any cars in our list!")
