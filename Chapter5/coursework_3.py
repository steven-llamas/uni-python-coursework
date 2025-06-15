instructor_1 = {
    "name": "blythe",
    "course": "csc24400",
}  # dictionary defined with 2 K-V pairs

print(instructor_1["name"])  # access and display value of key 'name'
print(instructor_1["course"])  # access and display value of key 'course'

new_course = instructor_1["course"]
print(f"\nYou need to enroll in {new_course} for next semester !")

instructor_1["age"] = 41  # adding third pair in our dictionary
instructor_1["office"] = "young316"  # adding fourth pair in our dictionary

print("\n")
print(instructor_1)  # print the modified dictionary, to see the two additional pairs
