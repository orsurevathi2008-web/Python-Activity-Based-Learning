
# Traffic Violation Penalty Calculator

n = int(input("Enter number of violations: "))

total_fine = 0
repeat_count = 0
disqualified = False

for i in range(n):

    print("\nViolation", i + 1)

    print("1. Two Wheeler")
    print("2. Four Wheeler")
    print("3. Heavy Vehicle")

    vehicle = int(input("Enter vehicle category: "))

    print("\nOffence Types")
    print("1. No Helmet")
    print("2. Overspeeding")
    print("3. Signal Jumping")
    print("4. Drunk Driving")
    print("5. Driving Without Licence")

    offence = int(input("Enter offence type: "))

    repeat = input("Is it a repeat offence? (yes/no): ")

    # Calculate basic fine
    if offence == 1:
        fine = 500
        offence_name = "No Helmet"

    elif offence == 2:
        fine = 1000
        offence_name = "Overspeeding"

    elif offence == 3:
        fine = 1000
        offence_name = "Signal Jumping"

    elif offence == 4:
        fine = 10000
        offence_name = "Drunk Driving"

    elif offence == 5:
        fine = 5000
        offence_name = "Driving Without Licence"

    else:
        print("Invalid offence")
        continue

    # Repeat offence penalty
    if repeat == "yes":
        fine = fine * 2
        repeat_count = repeat_count + 1

    # Disqualification conditions
    if offence == 4:
        disqualified = True

    total_fine = total_fine + fine

    print("\nVehicle Category:", vehicle)
    print("Offence:", offence_name)
    print("Final Fine: Rs.", fine)

# Check final disqualification status
if repeat_count >= 3:
    disqualified = True

print("\n----- FINAL REPORT -----")
print("Total Violations:", n)
print("Total Fine: Rs.", total_fine)

if disqualified:
    print("Driver Disqualification Condition: YES")
else:
    print("Driver Disqualification Condition: NO")

