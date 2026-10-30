
# Progressive Electricity Billing

n = int(input("Enter number of months: "))

bills = []

for i in range(n):
    print("\nMonth", i + 1)

    units = int(input("Enter electricity units: "))

    # Calculate slab charges
    if units <= 100:
        energy_charge = units * 1.50

    elif units <= 200:
        energy_charge = (100 * 1.50) + ((units - 100) * 2.50)

    elif units <= 500:
        energy_charge = (100 * 1.50) + (100 * 2.50) + ((units - 200) * 4.00)

    else:
        energy_charge = (100 * 1.50) + (100 * 2.50) + (300 * 4.00) + ((units - 500) * 6.00)

    # Fixed charge
    fixed_charge = 50

    # Calculate subtotal
    subtotal = energy_charge + fixed_charge

    # Surcharge and rebate
    surcharge = subtotal * 5 / 100
    rebate = subtotal * 2 / 100

    # Final bill
    total_bill = subtotal + surcharge - rebate

    bills.append(total_bill)

    print("Energy Charge:", round(energy_charge, 2))
    print("Fixed Charge:", fixed_charge)
    print("Surcharge:", round(surcharge, 2))
    print("Rebate:", round(rebate, 2))
    print("Total Bill:", round(total_bill, 2))

# Compare monthly bills
print("\n----- Monthly Bill Comparison -----")

for i in range(n):
    print("Month", i + 1, "Bill: Rs.", round(bills[i], 2))

    if i > 0:
        increase = bills[i] - bills[i - 1]

        if increase > 0:
            percentage = (increase / bills[i - 1]) * 100

            print("Bill Increase:", round(percentage, 2), "%")

            if percentage > 20:
                print("Warning: Unusual increase in electricity bill!")

        else:
            print("No increase in electricity bill.")

