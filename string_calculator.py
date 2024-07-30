def add(numbers):
    # Handle empty input string
    if not numbers:
        return 0

    # Check for custom separator
    if numbers.startswith("//"):
        lines = numbers.split("\n")
        separator = lines[0][2:]
        numbers = lines[1]
        numbers = numbers.replace("\n", separator).split(separator)
    else:
        # Replace newlines with commas and split the input string into numbers
        numbers = numbers.replace("\n", ",").split(",")

    # Convert the numbers to integers and filter out empty numbers
    numbers = [int(num) for num in numbers if num]

    # Check for negative numbers and raise an error if found
    negative_value = [num for num in numbers if num < 0]
    if negative_value:
        raise ValueError(f"Negative numbers not allowed: {', '.join(map(str, negative_value))}")

    # Return the sum of all numbers less than or equal to 1000
    return sum(num for num in numbers if num <= 1000)

