my_cars = ["toyota", "tesla", "hyundai", "audi", "porsche"]
friend_cars = my_cars[:]  # slice that includes the entire original list

print("\nMy favorite cars are: ")
print(my_cars)
print("\nMy friend's favorite cars are: ")
print(friend_cars)  # Both list contain same cars

# To prove we have two lists, we add a new car to each list
my_cars.append("bmw")
friend_cars.append("nissan")
print("\nMy favorite cars are: ")
print(my_cars)
print("\nMy friend's favorite cars are: ")
print(friend_cars)

# Same list (with two variables)
my_cars = ["toyota", "tesla", "hyundai", "audi", "porsche"]
friend_cars = my_cars  # instead of storing a copy, we set friend_cars equal to my_cars
my_cars.append("bmw")

print("\nMy favorite cars are: ")
print(my_cars)
print("\nMy friend's favorite cars are: ")
print(friend_cars)  # output shows both list are same, which is not we wanted
