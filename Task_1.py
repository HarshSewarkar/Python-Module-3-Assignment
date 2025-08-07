# Get an integer from the user
try:
    number = int(input("Enter an integer: "))

    # Check if the number is even or odd using the modulo operator
    if number % 2 == 0:
        print(f"The number {number} is even.")
    else:
        print(f"The number {number} is odd.")

except ValueError:
    print("Invalid input. Please enter a valid integer.")
