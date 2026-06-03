choice = 0

while choice != 4:
    print("1-Calculate net pay")
    print("2-Enter revenue or expense")
    print("3-Show discretionary income")
    print("4-Exit")

    choice = int(input("Choice: "))

    if choice == 4:
        print("Thanks for using My Finance!")
if choice == 1:
    wage = float(input("What is your hourly wage? "))
    hours = float(input("How many hours did you work? "))

    gross_pay = wage * hours

    federal_tax = gross_pay * 0.10
    state_tax = gross_pay * 0.05
    social_security = gross_pay * 0.062

    net_pay = gross_pay - federal_tax - state_tax - social_security
elif choice == 2:
    another = "Y"

    while another.upper() == "Y":
        name = input("Enter transaction name: ")
        amount = float(input("Enter amount (use negative sign for expense): "))

        if amount >= 0:
            revenue += amount
        else:
            expenses += amount

        another = input("Another? (Y/N): ")
elif choice == 3:
    discretionary = revenue + expenses

    print(
        f"Revenue: ${revenue:.2f} "
        f"Expenses: ${expenses:.2f} "
        f"Discretionary: ${discretionary:.2f}"
    )
    print()
    print(f"Gross Pay: ${gross_pay:.2f} ({hours} hours @ ${wage:.2f}/hr)")
    print(f"Federal tax: ${federal_tax:.2f}")
    print(f"State tax: ${state_tax:.2f}")
    print(f"Social security: ${social_security:.2f}")
    print(f"Net pay: ${net_pay:.2f}")
    print()
revenue = 0
expenses(0)