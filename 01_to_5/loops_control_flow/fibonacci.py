# Maximum value for the Fibonacci sequence
MAX_VALUE = 10000

# Starting values for the Fibonacci sequence
a, b = 0, 1

# Loop until the value of a is greater than or equal to MAX_VALUE
while a < MAX_VALUE:
    print(a, end=" ")
    a, b = b, a + b
