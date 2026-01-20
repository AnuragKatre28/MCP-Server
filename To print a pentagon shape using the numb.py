def print_pentagon(n: int) -> None:
    """
    Print a pentagon shape using numbers from 1 to n.

    Parameters:
    n (int): The maximum number to print in the pentagon. Must be between 1 and 5.

    Raises:
    ValueError: If n is not in the range of 1 to 5.
    """
    # Validate input
    if not (1 <= n <= 5):
        raise ValueError("Input must be between 1 and 5 inclusive.")

    # Calculate the number of rows in the pentagon
    rows = n + 1

    # Loop through each row to print the pentagon shape
    for i in range(rows):
        # Calculate leading spaces for formatting
        spaces = ' ' * (rows - i - 1)
        
        # Generate the number sequence for the current row
        numbers = ' '.join(str((j % n) + 1) for j in range(i + 1))
        
        # Print the formatted row with leading spaces
        print(spaces + numbers)

# Example usage
try:
    print_pentagon(5)
except ValueError as e:
    print(e)
