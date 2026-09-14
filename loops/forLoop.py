# fruits = ['banana', 'apple', 'cherry']
# for a in fruits:
#     print(a)

# students = ['ahmed', 'ali', 'saad']
# for name in students:
#     print ('welcom to class:', name)

# for i in range(1,6):
#     print ('ittration', i)

# my_name = 'i am batman i live in the shadows darkness is my ally'
# my_name_2 = my_name.split(" ")
# for i in my_name_2:
#     print(i)

# numbers = [5, 10, 15, 20]
# sum =  0
# for i in numbers:
#     sum = sum + i
#     print ("total sum =",sum)

# table = int(input('enter number to print table: '))
# for i in range(1,11):
#     print(table, 'x', i, '=', table*i)


# Task 1: Even Numbers
# num = [1,2,3,4,5,6,7,8,9,10]
# for i in num:
#     if i % 2 == 0:
#         print (i)

# Task 3: Count Vowels
# word = 'prigraming'
# count =0 
# for ch in word:
#     if ch in 'aeiou':
#         count +=1
#         print ('number of vowels:',count)

# Task 2: Squares of Numbers
# for i in range (1,11):
#     print('the squarea are:', i**2)

# Task 4: Reverse a String
# text = 'python'
# reverse = ''


# 1:Print all numbers from 1 to 15 and show their cubes.
# for i in range(1,16):
#     print ('the cubes are:', i**3)

# 2:Print only the names that start with ‘A’ from this 
# list = ['Ali', 'Sara', 'Asad', 'Hina', 'Ahsan']
# for name in list:
#     if name.startswith('A'):
#         print(name)

# 3:Write a loop to find the sum of all even numbers between 50 and 100.
# total = 0
# for i in range(50, 101):
#     if i % 2 == 0:
#         total += i
# print(total)

# 4:Write a for loop to count how many uppercase letters are in 'HelloPYTHON'.
# text = 'HelloPYTHON'
# count = 0
# for char in text:
#     if char.isupper():
#         count += 1
# print(count)

# 5:Use a for loop to print this pattern:
# for i in range(1, 6):
#     print("*" * i)

# 6:Print numbers from 10 down to 1 using a for loop.
# for i in range(10, 0, -1):
#     print(i)

# 7:Create a list of marks [78, 55, 90, 67, 82] and print 'Pass' if mark ≥ 60, otherwise 'Fail'.
# marks = [78, 55, 90, 67, 82]

# for mark in marks:
#     if mark >= 60:
#         print(mark, "Pass")
#     else:
#         print(mark, "Fail")

# 8:Write a program to print all elements of this list in reverse order: ['red', 'green', 'blue', 'yellow']
# colors = ['red', 'green', 'blue', 'yellow']
# for i in range(len(colors) - 1, -1, -1):
#     print(colors[i])

# 9:Use a nested for loop to print multiplication tables from 2 to 5.
# for i in range(2, 6):
#     print("Table of", i)
#     for j in range(1, 11):
#         print(i, "x", j, "=", i * j)
#     print()

# 10:Write a for loop to print all characters that are not vowels from 'education'.
text = 'education'
for char in text:
    if char not in 'aeiou':
        print(char)