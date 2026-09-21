movie = ('avengers','seven','doctor do little','intersteller','inception')
print(movie[2])
print(movie[4])

movie = ('avengers','seven','doctor do little','intersteller','inception')
length = len(movie)
print(length)

mixed_data_type = ('avengers',-34, True ,4,'inception')
print(mixed_data_type)

num = (10, 20, 10, 30, 10)
print('count of 10:' , num.count(10))  

data = (10, 20, 30, 40, 50)
print('index of 50:' ,data.index(50))

t = (1, 2, 3, 4, 5, 6, 7)
print(t[2:6])

lst = [1, 2, 3]
tup = tuple(lst)
print (tup)

student = ('Ali', 22, 'Karachi')
name, age, city = student
print(name, age, city)

nums = (10, 20, 30, 40)
print (70 in nums)

t1 = (1, 2, 3)
t2 = (4, 5, 6)
t3 = t1 + t2
print(t3)


# 1:Create a tuple of your 5 favorite cities and print the first and last city.
city = ('quetta','multan','karachi','islamabad','lahore')
print(city[2])
print(city[4])

# 2:Find the maximum and minimum value in a numeric tuple (34, 7, 99, 12, 56).
tuple = (34, 7, 99, 12, 56)
print(max(tuple))
print(min(tuple))

# 3:Create a nested tuple that contains your name and marks in 3 subjects, then print the second subject's mark.
tuple = (('ahmed'), (34, 21, 56))
print(tuple[1][1])

# 4:Convert a tuple (10, 20, 30) into a list, append 40 to the list, and convert it back into a tuple.
t = (10, 20, 30)
lis = list(t)
lis.append(40)
tup = tuple(lis)
print(tup)

# 5: Write a Python program to check if the number 50 exists in the given tuple (10, 20, 30, 40, 50).
tuple = (10, 20, 30, 40, 50)
if 50 in tuple:
    print('50 is in tuple')
else:
    ('no in tuple')