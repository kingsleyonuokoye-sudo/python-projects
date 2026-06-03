import math

# Loop so the user can enter multiple numbers
while True:

    # Ask the user for a whole number
    number = int(input("Enter a whole number (i.e., an integer): "))

    print(f"\nThe number you entered is {number}.")

    # Determine if the number is even or odd
    if number % 2 == 0:
        print(f"{number} is an even number.")
    else:
        print(f"{number} is an odd number.")

    # Determine if the number has a perfect square root
    square_root = math.isqrt(number)

    if square_root * square_root == number:
        print(f"{number} has a perfect square root.")
    else:
        print(f"{number} does not have a perfect square root.")

    # Find all factors of the number
    factors = []

    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(str(i))

    # Display the factors
    print(f"The factors of {number} are {','.join(factors)}.")

    # Ask if the user wants to continue
    again = input("\nWould you like to enter another number? ").upper()

    if again != "Y":
        print("\nThank you for playing!")
        break
    