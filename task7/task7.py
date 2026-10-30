
# Campus Resource Allocation Under Constraints

n = int(input("Enter number of activities: "))

available = int(input("Enter total available equipment: "))

activities = []

# Enter activity details
for i in range(n):

    print("\nActivity", i + 1)

    name = input("Enter activity name: ")
    required = int(input("Enter required equipment: "))
    priority = int(input("Enter priority (1 = Highest): "))

    activities.append([name, required, priority])

# Sort activities based on priority
activities.sort(key=lambda x: x[2])

print("\n----- RESOURCE ALLOCATION REPORT -----")

total_allocated = 0

# Allocate equipment
for activity in activities:

    name = activity[0]
    required = activity[1]
    priority = activity[2]

    if available >= required:
        allocated = required
    else:
        allocated = available

    shortage = required - allocated

    available = available - allocated
    total_allocated = total_allocated + allocated

    print("\nActivity:", name)
    print("Priority:", priority)
    print("Required Equipment:", required)
    print("Allocated Equipment:", allocated)
    print("Shortage:", shortage)

    if shortage == 0:
        print("Status: Fully Allocated")
    else:
        print("Status: Partially Allocated")

# Final report
print("\n----- FINAL REPORT -----")
print("Total Allocated Equipment:", total_allocated)
print("Remaining Equipment:", available)

print("\nResource Allocation Completed.")

