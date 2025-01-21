# Calculate the square of a list of numbers and print the results
def calculate_squares(numbers):
    """
    Calculate the square of each number in a list.
    
    Args:
        numbers (list): List of numerical values.
        
    Returns:
        list: A list of squared values.
    """
    return [number ** 2 for number in numbers]

# Example usage
if __name__ == "__main__":
    input_numbers = [3, 5, 7, 9]
    squared_numbers = calculate_squares(input_numbers)
    print("Squared Numbers:", squared_numbers)