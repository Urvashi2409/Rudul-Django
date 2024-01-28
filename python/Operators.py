# operators

# 1. Arithematic operators = "+, -, *, /. %, **, //"

# print(3 + 2)

# print(3 - 2)

# print(3*2)

# print(3/2)

# print(23+10)
# print(23-10)
# print(23*10)
# print(23/10)
# print(23%10)
# print(23**10)
# print(23//10)

# % (module operator gives remainder)

# print(3%2)

# print(7%3)

# print(9%5)

# print(7%4)

# print(10%6)

# print(12%10)

# print(15%3)

# print(12%4)

# print(3%4)

# print(5%7)

# print(25%50)

# print(24%11)

# print(11/5)
# floating point answer

# print(11//5)
# integer answer

# print(2**3)

# print(2**2)

# print(2**5)

# ** gives you exponentiation
# 2**3 -> 2^3

# 2. assignment operators
# =, +=, -=, *=, /=, **=, //, %=

# x = 5
# print(x)
# x += 2
# print(x)
# x -= 1
# print(x)
# x *= 3
# print(x)

# x /= 6
# print(x)
# x **= 2
# print(x)
# x //= 4
# print(x)
# x %= 3
# print(x)

# 3. Relational or comparison operators
# ==, !=, >, <, >=, <=

# if 3 < 4 and 5 > 3:
#       if 4 > 0 or 5 == 8:
#           print("Nested")
#       if 7 >= 6 or 3 != 0:
#         print("nested again")
#       elif (5 - 4) <= 0:
#         print("23")
#       else:
#         print("nested default")
# else:
#     ("outside")

# We us relational operators while using conditional statements
# to compare numbers or variables

# Logical Operators
# and, or, not

# if not(4 > 6) and not(8 > 5):
#     print("one")
# elif 4 > 5 or not(5 == 5):
#     print("two")
# else:
#     print("none")

# We us logical operators in conditional statement 
# when we need to check more thsn one conditon

# Identity Operators
# is, is not

# x = 12
# y = 12

# print(x is y)
# print(y is x)

# print(x is not y)
# print(y is not x)

# str1 = "Megan"
# str2 = "megan"

# print(str1 is str2)
# print(str2 is str1)

# print(str1 is not str2)
# print(str2 is not str1)

# Identity operator checks thhe case-sensitivity

# str1 = "21"
# num = 21

# print(str1 is num)
# print(num is str1)

# str1 is a string and num is an integer
# Both of them contains same value but they are not identcal

# list1 = ["apple", "mango"]
# list2 = ["apple", "mango"]

# print(list1 is list2)
# print(list2 is list1)

# list3 = list1

# print(list3 is list1)
# print(list1 is list3)

# print(list1 == list2)
# print(list3 == list1)

# is operator checks in the lists are exactly 
# identical by checking if they are stored at the same place
# but == operator checks if the lists conatains exact same elements in it

# Membership Operator
# in, not in

# mylist = [1, 2, 12, 24, 30, 15]

# print(12 in mylist)
# print(15 not in mylist)
# print(11 in mylist)
# print(16 not in mylist)

# Membership operator checks if an element is present in the list or not

# Bitwise Operators
# Decimal numbers
# Which are made up of digits from 0 to 9

# Binary numbers
# Which are made up of digits made up of digits 0 and 1

# Binary to decimal

# 10 -> 2

# 11 -> 3

# 111 -> 7

# 101 -> 5

# 110 -> 6

# 100 -> 4

# 010 -> 2

# 011 -> 3

# Bitwise & Operators

# 10 -> 2
# print(2&3)

# 001 -> 1
# print(3&5)

# 000 -> 0
# print(4&3)

# 10 -> 2
# print(2&2)

# 000 -> 0
# print(4&1)

# 0 -> 0
# print(1&0)

# 000 -> 0
# print(2&5)


# 2 or 3 -> 3
# print(2 | 3)

# 3 or 5 -> 7
# print(3 | 5)

# 4 or 3 -> 7
# print(4 | 3)

# 2 or 2 -> 2
# print(2 | 2)

# 4 or 1 -> 5
# print(4 | 1)

# 1 or 0 -> 1
# print(1 | 0)

# 2 or 5 -> 7
# print(2 | 5)

# Bitwise ~ Operator

# ~ 3 -> 0
# print(~3)

# ~ 7 -> 0
# print(~7)

# ~ 4 -> 3
# print(~4)

# ~ 12 -> 3
# print(~12)

# ~ 9 -> 6
# print(~9)

# ~ 8 -> 7
# print(~8)

# Left Shift Operator (<<)
