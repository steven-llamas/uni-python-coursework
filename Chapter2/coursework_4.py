cars = ["toyota", "tesla", "hyundai", "audi", "porsche"]
print("CARS LIST OF 5 CARS WE INITIALLY HAVE")
print(cars)

cars[0] = "nissan"  # Modify first list element
print("1. List after modifying 1st element: ")
print(cars)

cars.append("bmw")  # Add element to list end
print("2. List after adding element at the end: ")
print(cars)

cars.insert(0, "ford")  # Insert element to list
print("3. List after inserting a new element at position 0: ")
print(cars)

del cars[0]  # Removing list item at index 0
print("4. List after removing item at index 0, no longer acess to that removed value: ")
print(cars)

popped_cars = cars.pop()  # Popping list value and stroing in a variable
print("5. List after popping item: ")
print(cars)
print("6. The popped value of the list, that we have still access: ")
print(popped_cars)

cars.remove("porsche")  # Removing list item at via value
print("7. List after removing item with value 'porsche': ")
print(cars)
