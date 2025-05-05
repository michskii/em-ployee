# Program to find the symmetric difference between two sets

def find_symmetric_difference(set1, set2):
    return set1.symmetric_difference(set2)

# Example usage
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

symmetric_difference = find_symmetric_difference(set1, set2)
print("Symmetric Difference:", symmetric_difference)