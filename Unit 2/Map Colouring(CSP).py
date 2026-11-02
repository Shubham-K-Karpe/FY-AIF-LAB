
# CLASSROOM ALLOCATION USING CSP

# List of courses
courses = ["Python", "Maths", "Physics", "Chemistry"]

# Number of students and time slots for each course
course_details = {
    "Python": {"students": 40, "time": 1},
    "Maths": {"students": 35, "time": 1},
    "Physics": {"students": 50, "time": 2},
    "Chemistry": {"students": 25, "time": 2}
}

# Available classrooms and their capacities
classrooms = {
    "Room A": 40,
    "Room B": 50,
    "Room C": 30
}

# Dictionary to store classroom assignments
assignment = {}


# Function to check constraints
def is_valid(course, room):

    # Checking classroom capacity
    if classrooms[room] < course_details[course]["students"]:
        return False

    # Checking scheduling conflicts
    for assigned_course in assignment:

        if assignment[assigned_course] == room:

            if course_details[course]["time"] == course_details[assigned_course]["time"]:
                return False

    return True


# CSP using Backtracking
def solve(index):

    # All courses are assigned
    if index == len(courses):
        return True

    course = courses[index]

    # Trying available classrooms
    for room in classrooms:

        if is_valid(course, room):

            assignment[course] = room

            # Assigning the next course
            if solve(index + 1):
                return True

            # Backtracking
            del assignment[course]

    return False


# Main Program
print("================================")
print("    CLASSROOM ALLOCATION SYSTEM")
print("================================")

if solve(0):

    print("\nClassroom Allocation Successful!")

    print("\nFinal Classroom Assignments:")

    for course in courses:

        print(course, "->", assignment[course])

    print("\nAll Constraints Satisfied!")

else:

    print("\nNo Valid Classroom Allocation Found!")
