# Create a program that stores a student's name and marks. Use a loop to process marks for 3 subjects, calculate the total and average, and determine whether the student passed.
# Conditions:
# Average ≥ 50 → Pass
# Average ≥ 80 → Excellent
# Otherwise → Fail

name = "Ahmed"
print(name)
marks = [75, 80, 65]
total = 0
for mark in marks:
    total = total + mark
print(total)
average = total / len(marks)

print(average)
if average >= 80:
    print('Excellent'),
if average >= 50:
    print('Pass'),
else:
    print("Fail")


# Create a program that stores a customer's name and a list of product prices.
# Use a loop to calculate the total price.
# Conditions:
# If total is greater than 5000 and the customer is a member → 20% discount.
# If total is greater than 5000 or the customer is a member → 10% discount.
# Otherwise → no discount.

# name = "Ahmed"
# prices = [1500, 2000, 1000]
# member = True
# total = 0
# for price in prices:
#     total = total + price
# print(total)

# if total > 5000 and member:
#     discount =  total * 0.20,
# if total > 5000 or member:
#     discount =  total * 0.10,
# else:
#     discount = 0

# final_price = total - discount
# print(final_price)
name = "Ahmed"
prices = [1500, 2000, 1000]
member = True
total = 0
for price in prices:
    total = total + price
print("Total:", total)
if total > 5000 and member:
    discount = total * 0.20
elif total > 5000 or member:
    discount = total * 0.10
else:
    discount = 0
final_price = total - discount
print("Discount:", discount)
print("Final price:", final_price)


# Create a program that stores an employee's name and starting salary.
# Use a loop to calculate the salary for 5 years. Increase the salary by 10% every year.
# Conditions:
# If salary becomes greater than 100,000 or the year reaches 5, print "Eligible for promotion".
# Otherwise print "Not eligible yet".

name = "Ali"
salary = 70000

for year in range(1, 6):
    salary = salary + (salary * 0.10)
    if salary > 100000 or year == 5:
        print("Eligible for promotion"),
    else:
        ('Not eligible yet')


# Create a program that stores a username and password.
# Use a loop to check every character in the password and count the number of digits.
# Conditions:
# Password must have at least 8 characters.
# It must contain @ or #.
# It must contain at least 2 numbers.
# If all conditions are true, print "Strong Password".

username = "Ahmed"
password = "Ahmed@123"
count = 0
for char in password:
    if char.isdigit():
        count = count + 1
if len(password) >= 8 and ('@' in password or '#' in password) and count >= 2:
    print('strong password')
else:
    print('waek password')


# Create a program that stores a person's name, daily steps, and calories burned for 7 days.
# Use a loop to calculate:
# Total steps
# Average steps
# Total calories
# Conditions:
# If average steps ≥ 10,000 and total calories ≥ 3,500 → "Excellent"
# If average steps ≥ 7,000 or total calories ≥ 2,500 → "Good"
# Otherwise → "Needs Improvement"

steps = [8000, 10000, 12000, 9000, 11000, 7000, 13000]
calories = [400, 500, 550, 450, 500, 350, 600]

total_steps = 0
total_calories = 0

for i in range(7):
    total_steps = total_steps + steps[i]
    total_calories = total_calories + calories[i]
average_steps = total_steps / 7
print("Total Steps:", total_steps)
print("Average Steps:", average_steps)
print("Total Calories:", total_calories)
if average_steps >= 10000 and total_calories >= 3500:
    print('Excellent')
if average_steps >= 7000 or total_calories >= 2500:
    print('Good')
else:
    ('Need Improvment')