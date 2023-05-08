def euclid_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Ask the user for two integers
a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))

# Find the GCD using the Euclidean algorithm
gcd = euclid_gcd(a, b)

# Print the GCD
print("The GCD of", a, "and", b, "is", gcd)
