# # Question 1 – Student Result Management System
# marks = [78, 65, 82, 55, 90]
# total = sum(marks)
# print ('The total marks are',total)
# average = total/len(marks)
# print('The average is',average)

# if average >= 80:
#     performance = 'Excellenet'
# elif average >= 60:
#     performance = 'Good'
# elif average >= 40:
#     performance = 'pass'
# else:
#     performance = 'fail'
# print("Performance:", performance)

# Question 2 – Online Shopping Discount System
# prices = [2500, 1800, 3200, 1500, 900]

# total = sum(prices)

# print("The total is", total)

# if total >= 10000:
#     discount = 20
# elif total >= 5000:
#     discount = 10
# else:
#     discount = 0
# print("Discount:", discount, "%")
# discount_amount = total * discount / 100
# print("Discount Amount:", discount_amount)
# final_amount = total - discount_amount
# print("Final Amount:", final_amount)

# Question 3 – Cinema Seat Availability System
# seats = ["A1", "A2", "A3", "B1", "B2"]
# seats = input('Enter seat number: ')
# if seats in seats:
#     print('avaliable seat')
# else:
#     print('not avaliable')

# Question 4 – Employee Performance Evaluation
# scores = [85, 72, 90, 65, 88]
# total = sum(scores)
# print ('The total score is: ',total)
# average = total/len(scores)
# print ('this is the average: ',average)

# if average >= 85:
#     performance = 'Outstanding'
# elif average >= 70:
#     performance = 'Good'
# elif average >= 50:
#     performance = 'Needs Improvement'
# else: 
#     performance= 'poor'
# print ('The employee perfoemance is: ',performance)

# Question 5 – Restaurant Menu and Order System
items = ["Burger", "Pizza", "Biryani", "Pasta"]
prices = [500, 1200, 450, 800]
item = input("Enter item name: ")

if item in items:
    index = items.index(item)
    print ("price:", prices[index])
else: 
    print('item not avaliable')

# Question 6 – Temperature Monitoring System
# temperatures = [38, 41, 35, 29, 42]

# first = temperatures[0]
# if first > 40:
#     classification = 'very hot'
# elif first >= 30:
#      classification = 'hot'
# else:
#      classification = 'cool'
# print ('the first temp is',first, '-', classification)

# middle = temperatures[2]
# if first > 40:
#     classification = 'very hot'
# elif first >= 30:
#      classification = 'hot'
# else:
#      classification = 'cool'
# print ('the second temp is',middle, '-', classification)

# last = temperatures[4]
# if first < 40:
#     classification = 'very hot'
# elif first >= 30:
#      classification = 'hot'
# else:
#      classification = 'cool'
# print ('the last temp is',last, '-', classification)


# Question 7 – Bank Transaction Classification System
# transactions = [5000, -2000, 15000]

# transaction = transactions[2]
# print("Transaction Amount:", transaction)

# if transaction > 0:
#     transaction_type = 'Deposit'
# else: 
#     transaction_type = 'Withdrawal'
# print("Transaction Type:", transaction_type)

# if transaction > 10000:
#     category = 'Large transaction'
# elif transaction >= 5000:
#     category = 'Medium Transaction'
# else:
#      category = 'Small Transaction'
# print(category)

# Question 8 – Student Attendance Management System
# attendance = ["P", "P", "A", "P", "A"]
# attended =  attendance.count('P')
# print ('Total attended are: ', attended)
# total_classes = len(attendance) 
# print ('total classes are: ',total_classes)
# percaentage = (attended / total_classes) *100
# print ('te percentage is: ',percaentage)

# if percaentage >= 80:
#      status = 'Eligible for Exam'
# elif percaentage >= 60:
#      status = 'Warning'
# else:
#      status = 'Not Eligible'
# print ('the status is: ', status)

# Question 9 – Grocery Store Inventory System
# products = ["Milk", "Bread", "Eggs", "Juice"]
# stock = [10, 0, 25, 3]

# product = input("Enter product name: ")

# if product in products:
#     index = product.index(product)
#     quantity = stock[index]
#     if quantity == 0:
#         status= 'out of stock'
#     elif quantity <= 5:
#         status = 'low stock'
#     else:
#         status = "In Stock"

#     print("Product:", product)
#     print("Available Quantity:", quantity)
#     print("Inventory Status:", status)
# else: 
#     print('stock not avaliable')

# Question 10 – Mobile Data Usage Monitoring System
# data_usage = [2.5, 4.2, 7.8, 3.1, 9.5, 5.6, 1.8]
# total = data_usage[0] + data_usage[1] + data_usage[2] + data_usage[3] + data_usage[4] + data_usage[5] + data_usage[6] 
# print ('the total is: ',total)

# if total >= 30:
#     Category = 'High Usage'
# elif total >= 30:
#     Category = 'Moderate Usage'
# else:
#     Category = 'Low Usage'
# print('the category is: ', Category)

# highest = data_usage[0]

# if data_usage[1] > highest:
#     highest = data_usage[1]
# if data_usage[2] > highest:
#     highest = data_usage[2]    
# if data_usage[3] > highest:
#     highest = data_usage[3]
# if data_usage[4] > highest:
#     highest = data_usage[4]
# if data_usage[5] > highest:
#     highest = data_usage[5]
# if data_usage[6] > highest:
#     highest = data_usage[6]

# print('the highest data usage is: ', highest)

# lowest = data_usage[0]

# if data_usage[1] < lowest:
#     lowest = data_usage[1]
# if data_usage[2] < lowest:
#     lowest = data_usage[2]    
# if data_usage[3] < lowest:
#     lowest = data_usage[3]
# if data_usage[4] < lowest:
#     lowest = data_usage[4]
# if data_usage[5] < lowest:
#     lowest = data_usage[5]
# if data_usage[6] <lowest:
#     lowest = data_usage[6]
# print('the lowest data usage is: ', lowest)