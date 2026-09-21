#1: Create a set of fruits and perform add, remove, and update.
fruit = {'apple', 'banana', 'pineapple'}
fruit.add('strawberry')
fruit.remove('banana')
fruit.update(['pomegranate', 'blueberry'])
print(fruit)

#2: Find common and unique subjects of two students.
st1 = {"Math", "English", "Physics", "Chemistry"}
st2 = {"Math", "English", "Computer", "Biology"}
common = st1.intersection(st2)
unique = st1.symmetric_difference(st2)
print("Common subjects:", common)
print("Unique subjects:", unique)

#3: Check if one set is a subset of another.
A = {1,2,3,4,5,6}
B = {1,2,3}
print ('B is a subset of a:', B.issubset(B))

#4: Convert a list into a set and count unique elements.
lst = [1,3,4,5,6]
unique_num = set(lst)
print(unique_num)
count = len(unique_num)
print(count)

#5: Check if two sets are disjoint.
A = {1,2,3,4,5}
B = {6,7,8,9,10}
if B.isdisjoint(A):
    print('Sets are not disjoint')
else:
    print('Sets are disjoint')