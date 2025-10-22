def add(a, b):
    """Add two numbers and return the result."""
    return a + b


def multiply(a, b):
    """Multiply two numbers and return the result."""
    return a * b


def is_even(num):
    """Check if a number is even."""
    return num % 2 == 0


def reverse_string(text):
    """Reverse a string."""
    return text[::-1]


def find_max(numbers):
    """Find the maximum number in a list."""
    if not numbers:
        return None
    return max(numbers)
