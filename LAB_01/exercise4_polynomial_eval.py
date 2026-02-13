def polynom_evaluation(coeffs, x):
    # Start with the coeffs of the highest power
    n = len(coeffs) - 1
    result = coeffs[n]

    # Create a loop backwards from (n-1) to 0
    # In Python, range(start, stop, step) 
    # goes from n-1 down to 0 (the -1 is the exclusive stop)
    for i in range(n - 1, -1, -1):
        result = coeffs[i] + (result * x)

    return result

# --- Example Usage ---
coeffs = [3, -2, 0, 5]  # P(x) = 3 - 2x + 0x^2 + 5x^3
x_val = 2.0

output = polynom_evaluation(coeffs, x_val)
print(f"The result of the polynomial evaluation is: {output}")
# Output: 39.0