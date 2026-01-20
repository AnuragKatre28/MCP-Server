
def print_multiplication_table(number: int, up_to: int = 10) -> None:
    """
    Prints the multiplication table for a given number.

    Parameters:
    number (int): The number for which the multiplication table is to be printed.
    up_to (int): The maximum multiplier (default is 10).

    Raises:
    ValueError: If 'number' or 'up_to' is not a positive integer.
    """
    # Validate input parameters
    if not isinstance(number, int) or not isinstance(up_to, int):
        raise ValueError("Both 'number' and 'up_to' must be integers.")
    if number <= 0 or up_to <= 0:
        raise ValueError("Both 'number' and 'up_to' must be positive integers.")
    
    print(f"Multiplication Table for {number}:\n")

    # Loop through the range to create the multiplication table
    for i in range(1, up_to + 1):
        result = number * i  # Calculate the product
        print(f"{number} x {i} = {result}")

# Example usage to print the multiplication table for 34
if __name__ == "__main__":
    try:
        print_multiplication_table(34)
    except ValueError as e:
        print(f"Error: {e}")
