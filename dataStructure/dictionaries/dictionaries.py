# Replace all None values with "Unknown"
employees = {
    "Ali": "HR",
    "Sara": None,
    "Usman": "IT",
    "Hina": None
}
for key, values in employees.items():
    if values is None:
        employees[key] = "Unknown"
print(employees)

# Count how many times each word appears in a sentence using a dictionary.
dic = "hwa to hwa nahi hwa to nahi hwa nahi hwa to nahi hwa"
word_count = {}
for word in dic.split():
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(word_count)


# Create a dictionary summarizing total students, average marks, and top scorer.
marks = {
    "Ali": 85,
    "Sara": 90,
    "Usman": 78,
    "Hina": 92
}

totalStudent = len(marks)
totalMarks = sum(marks.values())
avgMarks = totalMarks / totalStudent
topScore = max(marks, key = marks.get)

summary = {
    "totalStudent": totalStudent,
    "totalMarks": totalMarks,
    "avgMarks": avgMarks,
    "topScore": topScore
}
print(summary)


# Convert two lists into a dictionary using zip().

keys = ["Name", "Age", "City"]
values = ["Ali", 23, "Karachi"]
comb_dict = dict(zip(keys,values))
print (comb_dict) 

# Given a list of categories, count the frequency of each unique value.
features = ["Male", "Female", "Male", "Female", "Other"]
word_count = {}
for word in features:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(word_count)