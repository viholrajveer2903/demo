numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(squares) # Output: [1, 4, 9, 16, 25]

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers) # Output: [2, 4, 6]

words = ["hello", "world", "python"]
upper_words = [x.upper() for x in words]
print(upper_words) # Output: ["HELLO", "WORLD", "PYTHON"]

numbers = [1, 2, 3, 4]
tuples = [(x, x**2) for x in numbers]
print(tuples) # Output: [(1, 1), (2, 4), (3, 9), (4, 16)]

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_list = [x for row in matrix for x in row]
print(flat_list) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
