# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Validate input to ensure it is positive
if size <= 0:
    print("Please enter a positive integer.")
else:
    # Initialize a counter for the rows
    row = 0

    # Use a while loop to iterate through rows
    while row < size:
        # Use a for loop to print asterisks in a row
        for _ in range(size):
            print("*", end="")
        print()  # Move to the next line after a row is printed
        row += 1

