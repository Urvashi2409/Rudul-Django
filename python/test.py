"""
Create a Python script that takes an input variable named num_of_books (an integer representing the number of books a person has) and prints a message 
indicating the person's reading habit based on the following conditions:

"Not much of a reader" if the number of books is 0.
"Casual reader" if the number of books is 1-10.
"Avid reader" if the number of books is 11-50.
"Bookworm" if the number of books is 51-100.
"Bibliophile" if the number of books is more than 100.
You can assume that:

The input value is valid, i.e., num_of_books is a non-negative integer.
"""

# num_of_books = 5
# if num_of_books == 0:
#     print("not much of a reader")
# elif 0 <= num_of_books  < 10:
#     print("casual reader")
# elif 11 <= num_of_books < 50:
#     print("Avid reader")
# elif 51 <= num_of_books < 100:
#     print("Bookworm")
# else:
#     print("Bibliophile")

"""
    Age Category Classifier:
Problem: Write a Python program that categorizes a person's age group. Categories are: 
'Child' (< 13 years), 
'Teen' (13-19 years), 
Adult' (20-64 years), 
and 'Senior' (65 years and older).
"""
# age = 10
# if age < 13:
#     print("Child")
# elif 13 <= age < 19:
#     print("Teen")
# elif 20 <= age < 64:
#     print("Adult")
# else:
#     print("Senior")

"""
    Library Fine Calculator:
Problem: Write a Python program to calculate library fines. The fine is based on how many days a book is overdue. 
If a book is overdue by 1-5 days, the fine is $2 per day. 
If it is overdue by 6-10 days, the fine is $5 per day. 
For more than 10 days, the fine is $10 per day. 
However, if the user is a member of the library, the fine rates are halved.          
Input: Number of days overdue and a Boolean indicating membership status.
"""

num_of_days = 3
membership = False
cost = 0
if 1 <= num_of_days < 5:
    cost = 2
elif 6 <= num_of_days < 10:
    cost = 5
else:
    cost = 10
if membership == True:
    cost = cost / 2
print(cost)

# 1.
print("Hello, Python")

# 2.
age = 9
print(f"I am {age} years old.")

# 3.
print(5 + 3)

# 4.
color = input("What is your favorite color?: ")
print(f"Your favorite color is {color}.")

# 5.
first_name = "Megan"
last_name = "Nguyen"
print(f"{first_name} {last_name}")

# 6.
number = 4
if number > 5:
    print("Yes, it is greater!")
else:
    print("No, it is less.")

# 7.
for i in range(1, 6):
    print(i)