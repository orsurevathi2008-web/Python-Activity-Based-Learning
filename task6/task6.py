
# Food Waste Monitoring System

n = int(input("Enter number of days: "))

prepared_list = []
served_list = []
leftover_list = []
waste_list = []

limit = 10

for i in range(n):

    print("\nDay", i + 1)

    prepared = int(input("Enter prepared meals: "))
    served = int(input("Enter served meals: "))

    # Calculate leftover meals
    leftover = prepared - served

    # Calculate wastage percentage
    if prepared > 0:
        waste = (leftover / prepared) * 100
    else:
        waste = 0

    prepared_list.append(prepared)
    served_list.append(served)
    leftover_list.append(leftover)
    waste_list.append(waste)

    print("Leftover Meals:", leftover)
    print("Wastage Percentage:", round(waste, 2), "%")

    # Check acceptable limit
    if waste > limit:
        print("Excessive Food Waste")
    else:
        print("Acceptable Food Waste")

# Calculate total values
total_prepared = sum(prepared_list)
total_served = sum(served_list)
total_leftover = sum(leftover_list)

if total_prepared > 0:
    total_waste = (total_leftover / total_prepared) * 100
else:
    total_waste = 0

# Display final report
print("\n----- FOOD WASTE REPORT -----")

for i in range(n):
    print("\nDay", i + 1)
    print("Prepared Meals:", prepared_list[i])
    print("Served Meals:", served_list[i])
    print("Leftover Meals:", leftover_list[i])
    print("Wastage:", round(waste_list[i], 2), "%")

    if waste_list[i] > limit:
        print("Status: Excessive Waste")
    else:
        print("Status: Acceptable")

print("\nTotal Prepared Meals:", total_prepared)
print("Total Served Meals:", total_served)
print("Total Leftover Meals:", total_leftover)
print("Overall Wastage:", round(total_waste, 2), "%")

print("\nFood Waste Monitoring Completed.")

