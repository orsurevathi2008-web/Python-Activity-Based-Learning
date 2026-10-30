
rooms = []

n = int(input("Enter number of classrooms: "))

for i in range(n):
    name = input("Enter room name: ")
    capacity = int(input("Enter room capacity: "))
    rooms.append((name, capacity))

courses = []

m = int(input("\nEnter number of courses: "))

for i in range(m):
    course = input("Enter course name: ")
    students = int(input("Enter number of students: "))
    period = input("Enter period: ")
    courses.append((course, students, period))

allocated = []
used = []
not_allocated = []

for course, students, period in courses:
    found = False

    for room, capacity in rooms:
        if capacity >= students and (room, period) not in used:
            allocated.append((course, room, period))
            used.append((room, period))
            found = True
            break

    if found == False:
        not_allocated.append(course)

print("\nCLASSROOM TIMETABLE")

for course, room, period in allocated:
    print(course, "->", room, "->", period)

print("\nCourses not allocated:", not_allocated)

if len(not_allocated) == 0:
    print("All courses are accommodated.")
else:
    print("All courses cannot be accommodated.")

