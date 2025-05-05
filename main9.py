# Test dictionary
test_dict = {'codingal': 3, 'is': 2, 'for': 2, 'coding': 1}

# Value to check frequency
value_to_check = 2

# Count the frequency of the value
frequency = list(test_dict.values()).count(value_to_check)

print(f"The frequency of the value {value_to_check} is: {frequency}")