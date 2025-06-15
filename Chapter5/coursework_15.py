instructors = {
    "INST_1": {
        "fname": "david",
        "lname": "blythe",
        "course": "csc24400",
    },
    "INST_2": {
        "fname": "smith",
        "lname": "miller",
        "course": "csc45400",
    },
    "INST_3": {
        "fname": "mark",
        "lname": "lenka",
        "course": "csc46400",
    },
}  # nest dictionary inside another

for instNum, instInfo in instructors.items():  # loop through instructors dictionary
    print(f"\n Instructor: {instNum}")  # print instructor number, say INST_1
    full_name = (
        f"{instInfo['fname']} {instInfo['lname']}"  # start accessing inner dictionary
    )
    course_name = f"{instInfo['course']}"

    print(f"\t Full name: {full_name.title()}")  # print full name from inner dictionary
    print(
        f"\t Course: {course_name.upper()}"
    )  # print course name from inner dictionary
