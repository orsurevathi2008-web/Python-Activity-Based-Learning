
# Hospital Ward Occupancy Monitoring

wards = int(input("Enter number of wards: "))
days = int(input("Enter number of days: "))

ward_names = []
capacity = []
occupancy = []

# Enter ward details
for i in range(wards):

    name = input("\nEnter ward name: ")
    beds = int(input("Enter total bed capacity: "))

    ward_names.append(name)
    capacity.append(beds)

    daily = []

    for j in range(days):
        count = int(input("Enter occupied beds on day " + str(j + 1) + ": "))
        daily.append(count)

    occupancy.append(daily)

# Calculate ward utilization
print("\n----- WARD OCCUPANCY REPORT -----")

for i in range(wards):

    total = sum(occupancy[i])
    average = total / days
    percentage = (average / capacity[i]) * 100

    print("\nWard:", ward_names[i])
    print("Total Capacity:", capacity[i])
    print("Average Occupied Beds:", round(average, 2))
    print("Utilization Percentage:", round(percentage, 2), "%")

    # Check capacity violations
    for j in range(days):

        if occupancy[i][j] > capacity[i]:
            print("Capacity Violation on Day", j + 1)

# Calculate daily occupancy
daily_total = []

for j in range(days):

    total = 0

    for i in range(wards):
        total = total + occupancy[i][j]

    daily_total.append(total)

# Find peak demand
peak = max(daily_total)
peak_day = daily_total.index(peak) + 1

print("\n----- DAILY OCCUPANCY REPORT -----")

for j in range(days):
    print("Day", j + 1, "Total Occupied Beds:", daily_total[j])

print("\nPeak Demand Day:", peak_day)
print("Maximum Occupied Beds:", peak)

print("\nMonitoring Completed.")

