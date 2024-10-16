# Loop until a valid number is entered
while True:
    user_input = input("Enter a number: ")

    # Try to convert the input to an integer
    if user_input.lstrip('-').isdigit():
        number = int(user_input)
        total_digits = len(user_input.lstrip('-'))  # Count digits, ignoring the sign
        print(f"The total number of digits in {number} is {total_digits}.")
        break  # Exit the loop after a valid input
    else:
        print("Please enter a valid integer.")
