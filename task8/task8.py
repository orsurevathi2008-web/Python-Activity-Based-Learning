
# Smart Campus Incident and Maintenance Prioritization

n = int(input("Enter number of maintenance reports: "))

incidents = []

for i in range(n):

    print("\nIncident", i + 1)

    name = input("Enter incident name: ")
    location = input("Enter campus location: ")

    print("1. Low Severity")
    print("2. Medium Severity")
    print("3. High Severity")

    severity = int(input("Enter severity: "))

    frequency = int(input("Enter reported frequency: "))

    # Assign location priority
    if location.lower() == "laboratory":
        location_priority = 3

    elif location.lower() == "classroom":
        location_priority = 2

    else:
        location_priority = 1

    # Calculate priority score
    score = (severity * 10) + (frequency * 2) + location_priority

    incidents.append([name, location, severity, frequency, score])

# Sort incidents based on priority score
incidents.sort(key=lambda x: x[4], reverse=True)

# Display priority report
print("\n----- INCIDENT PRIORITY REPORT -----")

for i in range(n):

    print("\nRank:", i + 1)
    print("Incident:", incidents[i][0])
    print("Location:", incidents[i][1])
    print("Severity:", incidents[i][2])
    print("Frequency:", incidents[i][3])
    print("Priority Score:", incidents[i][4])

# Generate priority summary
print("\n----- PRIORITY SUMMARY -----")

high = 0
medium = 0
low = 0

for incident in incidents:

    if incident[4] >= 40:
        high = high + 1

    elif incident[4] >= 25:
        medium = medium + 1

    else:
        low = low + 1

print("High Priority Cases:", high)
print("Medium Priority Cases:", medium)
print("Low Priority Cases:", low)

if n > 0:
    print("Highest Priority Incident:", incidents[0][0])

print("\nMaintenance Monitoring Completed.")

