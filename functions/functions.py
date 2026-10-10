# Task 1:
# Write a function that takes a list of integers and returns a new list containing only the unique elements (remove duplicates).
def unique_num(numbers):
    return list(set(numbers))
numbers = [1, 2, 2, 3, 4, 4, 5]
result = unique_num(numbers)
print(result)


# Task 2:
# Write a function that takes a list of student marks and returns the highest mark.
def height_mark(marks):
    return max(marks)
marks = [85, 92, 78, 95, 88]
results = height_mark(marks)
print("height marks are:",results)


# Task 3:
# Write a function that takes a sentence and returns the number of words in it.
def num_words(sentence):
    words = sentence.split()
    return len(words)
sentence = "Python is easy to learn"
results = num_words(sentence)
print (results)


# Task 4 (Data Science Related):
# Write a function that takes a list of numbers and returns a list with each number standardized (subtract mean and divide by standard deviation).
def standardize(numbers):
    mean = sum(numbers) / len(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    standard_deviation = variance ** 0.5
    standardized = []
    for x in numbers:
        value = (x - mean) / standard_deviation
        standardized.append(value)
    return standardized
numbers = [10, 20, 30, 40, 50]
result = standardize(numbers)
print(result)

# Task 5:
# Write a lambda function to calculate the cube of a number.
cube = lambda x: x ** 3
print(cube(5))