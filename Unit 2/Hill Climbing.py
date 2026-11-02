
# EXAM TIMETABLE OPTIMIZATION USING HILL CLIMBING

# List of examinations
exams = ["Maths", "Physics", "Chemistry", "Programming"]

# Students appearing for different exams
students = {
    "Maths": ["A", "B", "C"],
    "Physics": ["A", "B"],
    "Chemistry": ["C", "D"],
    "Programming": ["A", "D"]
}

# Faculty assigned to examinations
faculty = {
    "Maths": "F1",
    "Physics": "F2",
    "Chemistry": "F1",
    "Programming": "F3"
}

# Available time slots
slots = [1, 2, 3]


# Function to count scheduling conflicts
def calculate_conflicts(timetable):

    conflicts = 0

    for i in range(len(exams)):

        for j in range(i + 1, len(exams)):

            exam1 = exams[i]
            exam2 = exams[j]

            # Checking if exams have the same time slot
            if timetable[exam1] == timetable[exam2]:

                # Checking common students
                for student in students[exam1]:

                    if student in students[exam2]:
                        conflicts = conflicts + 1
                        break

                # Checking common faculty
                if faculty[exam1] == faculty[exam2]:
                    conflicts = conflicts + 1

    return conflicts


# Hill Climbing Function
def hill_climbing():

    # Initial timetable
    timetable = {
        "Maths": 1,
        "Physics": 1,
        "Chemistry": 2,
        "Programming": 2
    }

    print("Initial Timetable:", timetable)

    current_conflicts = calculate_conflicts(timetable)

    print("Initial Conflicts:", current_conflicts)

    # Hill Climbing process
    while current_conflicts > 0:

        improved = False

        for exam in exams:

            old_slot = timetable[exam]

            for slot in slots:

                if slot != old_slot:

                    timetable[exam] = slot

                    new_conflicts = calculate_conflicts(timetable)

                    # Keeping the better timetable
                    if new_conflicts < current_conflicts:

                        current_conflicts = new_conflicts
                        improved = True
                        print("\nImproved Timetable:", timetable)
                        print("Conflicts:", current_conflicts)
                        break

                    else:

                        timetable[exam] = old_slot

            if improved:
                break

        # Stopping if no improvement is possible
        if not improved:
            break

    return timetable, current_conflicts


# Main Program
print("===================================")
print("   EXAM TIMETABLE OPTIMIZATION")
print("===================================")

result, conflicts = hill_climbing()

print("\nFinal Examination Timetable:")

for exam in exams:
    print(exam, ":", "Slot", result[exam])

print("\nTotal Scheduling Conflicts:", conflicts)

if conflicts == 0:
    print("Timetable successfully optimized!")
else:
    print("Local optimum reached. Some conflicts remain.")
