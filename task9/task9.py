
# Disaster Relief Supply Allocation

n = int(input("Enter number of affected areas: "))

available = int(input("Enter total available relief supplies: "))

areas = []

# Enter area details
for i in range(n):

    print("\nArea", i + 1)

    name = input("Enter area name: ")
    required = int(input("Enter required supplies: "))
    priority = int(input("Enter priority (1 = Highest): "))

    areas.append([name, required, priority])

# Sort according to priority
areas.sort(key=lambda x: x[2])

print("\n----- RELIEF ALLOCATION REPORT -----")

total_allocated = 0
total_unmet = 0

# Allocate supplies
for area in areas:

    name = area[0]
    required = area[1]
    priority = area[2]

    if available >= required:
        allocated = required
    else:
        allocated = available

    unmet = required - allocated

    available = available - allocated

    total_allocated = total_allocated + allocated
    total_unmet = total_unmet + unmet

    print("\nArea:", name)
    print("Priority:", priority)
    print("Required Supplies:", required)
    print("Allocated Supplies:", allocated)
    print("Unmet Demand:", unmet)

    if unmet == 0:
        print("Status: Fully Supplied")
    else:
        print("Status: Partially Supplied")

# Final report
print("\n----- FINAL REPORT -----")

print("Total Allocated Supplies:", total_allocated)
print("Total Unmet Demand:", total_unmet)
print("Remaining Stock:", available)

print("\nDisaster Relief Allocation Completed.")

