while True:
    number = int(input("Enter a number: "))

    print(f"Factors of {number} are:")

    for i in range(1, number + 1):
        if number % i == 0:
            print(i)

            choice = input("Do you want to continue? (y/n): ")
            if choice.lower() == "no":
                break


import math

number = int(input("Enter a number: "))

root = math.sqrt(number)

if root == int(root):
    print(number, "is a perfect square.")
else:
    print(number, "is not a perfect square.")
    