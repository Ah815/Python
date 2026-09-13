# # for num1 in range(3):
# #     for num2 in range(2):
# #         print(f'i = {num1}, j = {num2}')
# #     print('------------')

# # words = ['HI', 'BYE']

# # for word in words:
# #     for char in word:
# #         print(char)
# #     print('-')

# for i in range(1,6):
#     for j in range(1,6):
#         print('teh value of i:',i,"The value of j:",j)
#     print('--------------------------------')

# for i in range(1,6):
#     for j in range(1,6):
#         print(i, '*', j, '=', i * j)
#     print('-----------')

# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# for row in matrix:
#     for item in row:
#         print (item, end = '')
#     print ('\n')

# for i in range(1,6):
#     for j in range(1,6):
#         if i == j:
#             print (f'i and j are equal: {i}')
#     print ('--------------------')

# for i in range(1,6):
#     for j in range(i):
#         print ('*', end = '')
#     print()

# for i in range(5,0,-1):
#     for j in range(j):
#         print ('*', end = '')
#     print()

# for i in range(1,6):
#     for j in range(1, i+1):
#         print(j, end = '')
#     print()

# for i in range(6,0,-1):
#     for j in range(1, i+1):
#         print(j, end = '')
#     print()


# class task 1
for i in range(1,5):
    for j in range(i):
        print (i, end = '')
    print()

# class task 2
nums = [[10,15,20],
        [25,30,35],
        [40,45,50]
        ]
for row in nums:
    for n in row:
        if n % 2 == 0:
            print(n, end=' ')
        # print()
# class task3
for i in range(1,4):
    for j in range(1,4):
        print(f'({i},{j})')

#class task 4
words = ['apple', 'mango']
for word in words:
    for ch in word:
        if ch in 'aeiou':
            print(ch, end='')
#class task 5
for i in range(1,6):
    for j in range(1,11):
        print(i, '*', j, '=', i * j)
    print('-----------')




# Print the following pattern:
for i in range(1,6):
    for j in range(i):
        print ('*',end='')
    print ()

#Print only odd numbers from a 2D list.
nums = [[10,15,20],
        [25,30,35],
        [40,45,50]
        ]
for row in nums:
    for n in row:
        if n % 2 != 0:
            print(n, end=' ')
        print()

#From list of strings ['hi', 'python'], print only consonants.
words = ['hi', 'python']
for word in words:
    for ch in word:
        if ch not in 'aeiou':
            print(ch, end='')
        print()

# Create a pattern of numbers like:
for i in range(1,6):
    for j in range(5, 5-i, -1):
        print(j, end = '')
    print()

#Print all pairs (i, j) where i + j is even.
for i in range(1,6):
    for j in range(1,6):
        if (i+j) %2==0:
            print ((i,j),"=",(i+j))
