favorite_cars = {
    "mackenzie": ["toyota", "bmw"],
    "danian": [
        "tesla",
        "audi",
    ],  # dictionary defined with two lists inside the dictionary
}

for (
    name,
    cars,
) in (
    favorite_cars.items()
):  # items() returns a list of K-V pairs, each value will be a list
    print(f"\n{name.title()}'s favorite cars are: ")
    for car in cars:  # nested for loop, one for D, another for L
        print(f"\t{car.upper()}")
