squares = [x**2 for x in range(1, 11)]
print("Squares:", squares)

evens = [x for x in range(1, 21) if x % 2 == 0]
print("Even numbers:", evens)

words = ["employee", "python", "code", "list"]
word_lengths = [len(word) for word in words]
print("Word lengths:", word_lengths)

names = ["alice", "bob", "charlie"]
uppercase_names = [name.upper() for name in names]
print("Uppercase names:", uppercase_names)

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
cartesian_product = [(x, y) for x in list1 for y in list2]
print("Cartesian product:", cartesian_product)