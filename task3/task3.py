
# Railway Fare and Reservation Calculator

n = int(input("Enter number of passengers: "))

total_amount = 0

for i in range(n):

    print("\nPassenger", i + 1)

    name = input("Enter passenger name: ")
    age = int(input("Enter age: "))
    distance = int(input("Enter distance in km: "))

    print("1. Sleeper")
    print("2. AC 3 Tier")
    print("3. AC 2 Tier")

    choice = int(input("Enter travel class: "))

    # Calculate distance-based fare
    if distance <= 100:
        basic = distance * 1

    elif distance <= 200:
        basic = 100 + (distance - 100) * 1.5

    else:
        basic = 100 + 150 + (distance - 200) * 2

    # Calculate class fare
    if choice == 1:
        fare = basic
        class_name = "Sleeper"

    elif choice == 2:
        fare = basic * 2
        class_name = "AC 3 Tier"

    elif choice == 3:
        fare = basic * 3
        class_name = "AC 2 Tier"

    else:
        print("Invalid class")
        continue

    # Age-based concession
    if age < 5:
        fare = 0

    elif age <= 12:
        fare = fare * 0.50

    elif age >= 60:
        fare = fare * 0.60

    # Reservation fee
    reservation = 40

    print("\n1. Booking")
    print("2. Cancellation")

    status = int(input("Enter ticket status: "))

    if status == 1:
        amount = fare + reservation
        print("\nTicket Booked Successfully")

    elif status == 2:
        amount = fare * 0.25
        print("\nTicket Cancelled")
        print("Cancellation Penalty:", amount)

    else:
        print("Invalid status")
        continue

    total_amount = total_amount + amount

    print("Passenger Name:", name)
    print("Travel Class:", class_name)
    print("Ticket Fare:", round(fare, 2))
    
    if status == 1:
        print("Reservation Fee:", reservation)

    print("Final Amount: Rs.", round(amount, 2))

print("\nTotal Amount for All Passengers: Rs.",
      round(total_amount, 2))

