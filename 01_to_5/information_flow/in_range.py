def in_range(n, low, high):
    """Returns True if n is between low and high, inclusive."""
    return low <= n <= high

# Test cases
print(in_range(5, 1, 10))  # True, because 5 is between 1 and 10
print(in_range(0, 1, 10))  # False, because 0 is less than 1
print(in_range(15, 1, 10)) # False, because 15 is greater than 10
print(in_range(7, 7, 7))   # True, because 7 is equal to both low and high
