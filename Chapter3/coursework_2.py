cars = ["toyota", "tesla", "hyundai", "audi", "porsche"]
print("\nInitial list of five cars: ")
print(cars)

print("\nHere are the first three cars on my list: ")
for car in cars[:3]:
    print(car.title())  # loops only first three cars
