# #add
# fruit = {"apple", "banana", "watermelon"}
# fruit.add("mango")
# print(fruit)

# #append
# fruit = ["apple", "banana", "watermelon"]
# fruit.append("mango")
# print(fruit)

# #insert
# fruit = ["apple", "banana", "watermelon"]
# fruit.insert(1,"mango")
# print(fruit)

# #extend (used to add multiple items but adds at the end)
# fruit = ["apple", "banana", "watermelon"]
# fruit1 = ["pineaple", "orange"]
# # more_fruit = ['mango', 'kiwi']
# # fruit.extend(more_fruit)
# fruit.extend(['mango', 'kiwi'])
# fruit1.extend(['mango', 'kiwi'])
# print (fruit,fruit1)

# #remove
# fruit = ["apple", "banana", "watermelon"]
# fruit.remove('banana')
# print (fruit)

# #pop (need to give index number to pop the item else the last item wil be poped)
# fruit = ["apple", "banana", "watermelon"]
# # removed_fruit = fruit.pop()
# removed_fruit = fruit.pop(1)
# print (fruit)

# #clear (will clear the item in teh list but the list will remain)
# fruit = ["apple", "banana", "watermelon"]
# fruit.clear()
# print (fruit)

# #Sort
# num = ['2','6','4','3','1','5']
# # num.sort()
# num.sort(reverse=True)
# print(num)

# #reverse
# num = ['2','6','4','3','1','5']
# num.reverse()
# print(num)

# #count (tell repitaion of specific elements)
# #index
# color = ('red', 'green', 'red', 'purple')
# print(color.index('red'))
# print(color.count('red'))

# #copy
# original = ['10', '20','30']
# copy_list = original.copy()
# original[1]=3
# print (copy_list)
# print (original)



#class task
name = ['ahmed', 'talha', 'murtaza', 'ali', 'fahad']
name.append('ahad')
print (name)
name.insert(2,'osama')
print (name)
name.remove('ahmed')
print (name)
name.sort()
print (name)


#Task 1: Create a list of numbers and use pop() to remove the last two items.
num = ['2','6','4','3','1','5']
num.pop(-1)
num.pop(-2)
print(num)

#Task 2: Make a list of 5 countries. Use insert() to add one at index 3, then use count() to count a specific country.
countries = ['Pakistan', 'Iran', 'India', 'UAE', 'Amarica']
countries.insert(3,'Pakistan')
print(countries)
print(countries.count('Pakistan'))

#Task 3: Create a list of integers. Use sort() and then reverse() to show them in descending order.
num = ['2','-6','4','-3','1','5']
num.sort()
print(num)
num.reverse()
print(num)

#Task 4: Use copy() to duplicate a list. Change one element in the copy and show that the original list remains unchanged.
countries = ['Pakistan', 'Iran', 'India', 'UAE', 'Amarica']
copy_list = countries.copy()
print (copy_list)
copy_list [1] = 'Africa'
print(copy_list)

#Task 5: Combine two lists of fruits and vegetables and check if 'apple' is present in the combined list.
fruits = ["apple", "banana", "mango"]
vegetables = ["potato", "carrot", "onion"]
fruits.extend(vegetables)
print (fruits)
print ("apple" in fruits)