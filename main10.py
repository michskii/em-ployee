from functools import reduce

# Function to calculate the product of all elements in a tuple
def calculate_product(tup):
    return reduce(lambda x, y: x * y, tup)

# Given tuples
tup1 = (4, 3, 2, 2, -1, 18)
tup2 = (2, 4, 8, 8, 3, 2, 9)

# Calculate and print the products
product_tup1 = calculate_product(tup1)
product_tup2 = calculate_product(tup2)

print(f"Product of tup1: {product_tup1}")
print(f"Product of tup2: {product_tup2}")