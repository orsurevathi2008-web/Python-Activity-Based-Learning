##Programme Statement

The aim of this program is to develop a Traffic Violation Penalty Calculator using Python. The program processes multiple traffic violations based on vehicle category, offence type and repeat-offence status. It calculates the fine amount using predefined penalty rules. It also identifies serious violations and checks whether the driver meets the disqualification conditions.

##Algorithm

1. Start the program.
   
2.Enter the number of traffic violations.   

3. Enter the number of traffic violations.
4. Calculate the basic fine based on the offence:
5. For each violation, enter:
6. f it is a repeat offence, double the basic fine.
7.Calculate the final penalty. 
   - Vehicle category (Two-wheeler, Four-wheeler or Heavy vehicle).
   - Offence type.
   - Repeat-offence status (Yes or No).
8. Calculate the basic fine based on the offence:
   - No helmet – ₹500.
   - Overspeeding – ₹1,000.
   - Signal jumping – ₹1,000.
   - Drunk driving – ₹10,000.
   - Driving without licence – ₹5,000.
9. Check whether the offence is repeated.
10. If it is a repeat offence, double the basic fine.
11. Calculate the final penalty.
12. Check disqualification conditions:
   - Drunk driving.
   - Three or more repeated violations.
11. Display the offence details and final penalty.
12. Calculate the total penalty for all violations.
13. Display the disqualification status.
14. Stop the program.
```mermaid

flowchart TD
    A([Start]) --> B[/Enter number of violations/]
    B --> C[/Enter vehicle category/]
    C --> D[/Enter offence type/]
    D --> E[/Enter repeat offence status/]
    E --> F[Find basic fine]
    F --> G{Repeat offence?}
    G -->|Yes| H[Double the fine]
    G -->|No| I[Keep basic fine]
    H --> J[Calculate final penalty]
    I --> J
    J --> K{Drunk driving or 3+ repeats?}
    K -->|Yes| L[Mark disqualification condition]
    K -->|No| M[No disqualification condition]
    L --> N[Add penalty to total]
    M --> N
    N --> O{More violations?}
    O -->|Yes| C
    O -->|No| P[Display total penalty and status]
    P --> Q([Stop])
```
##Sample input

Enter number of violations: 3

Violation 1

Enter vehicle category: 1

Enter offence type: 1

Is it a repeat offence? (yes/no): no

Violation 2

Enter vehicle category: 2

Enter offence type: 2

Is it a repeat offence? (yes/no): yes

Violation 3

Enter vehicle category: 3

Enter offence type: 4

Is it a repeat offence? (yes/no): no

##sample output

Violation 1

Vehicle Category: 1

Offence: No Helmet

Final Fine: Rs. 500

Violation 2

Vehicle Category: 2

Offence: Overspeeding

Final Fine: Rs. 2000

Violation 3

Vehicle Category: 3

Offence: Drunk Driving

Final Fine: Rs. 10000

----- FINAL REPORT -----

Total Violations: 3

Total Fine: Rs. 12500

Driver Disqualification Condition: YES

    
