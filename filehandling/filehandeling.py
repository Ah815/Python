# Task 1:
# Create a file named data.txt and write 5 random numbers into it.
# Then read and display those numbers.
with open("data.txt", "r") as f:
    print(f.read())

# Task 2:
# Write a program that reads a file and counts how many lines, words, and characters it has.
def count_file(filename):
    with open(filename, "r") as f:
        content = f.read()
        lines = content.splitlines()
        words = content.split()
        characters = len(content)
        return len(lines), len(words), characters
lines, words, characters = count_file("sample.txt")
print("Lines:", lines)
print("Words:", words)
print("Characters:", characters)

# Task 3:
# Write a program to read all student names from a file and print only those whose names start with the letter “A”.
def find_students(filename):
    with open(filename, "r") as f:
        for name in f:
            name = name.strip()
            if name.startswith("A"):
                print(name)
find_students("students.txt")

# Task 4:
# Write a program that copies the contents of data.txt into backup.txt only if data.txt exists.
try:
    with open("data.txt", "r") as source:
        content = source.read()
    with open("backup.txt", "w") as backup:
        backup.write(content)
    print("File copied successfully!")
except FileNotFoundError:
    print("data.txt does not exist.")

# Task 5:
# Create a log file error_log.txt that stores custom error messages using file handling.
with open("error_log.txt", "a") as f:
    f.write("Error: File not found.\n")
    f.write("Error: Invalid input.\n")
    f.write("Error: Something went wrong.\n")

print("Error messages saved successfully!")
