# Function is a template to organise is the code and make it reusable

# This is function definition and a,b are the parameters
# def add(a,b):
#     sum = a + b 
#     print(sum)

# this is function call, function will not excute without calling it
# add(13,8)

# we make the function once and call it for different values

# def divide(a,b):
    # quotient = a/b 
    # print(quotient)
# 
# divide(245,7)
# 
# def mulitply(a,b):
    # product = a*b 
    # print(product)
# 
# mulitply(45,9)

# def greater(a,b):
#     if a > b:
#         print("a is greater")
#     else:
#         print("b is greater")

# greater(42,902)
    
# def greatest(a,b,c):
#     if a > b and a > c:
#         print("a is the greatest")
#     elif b > a and b > c:
#         print("b is the greatest")
#     else:
#         print("c is the greatest")

# greatest(102, 307, 457)

# def information(name, age, place):
#     print(f"{name} is {age} years old and lives in {place}")

# information("Andy", 12, "Texas")

# mylist = [1,5,3,11,4,2,12]
# def sum(mylist):
#     sum = 0
#     for i in mylist:
#         sum += i
#     print(sum)

# sum(mylist)

# mylist = [1,5,3,11,4,2,12]
# def mul(mylist):
#     mul = 1
#     for i in mylist:
#         mul *= i
#     print(mul)

# mul(mylist)

# num = 10
# def range_num(num):
#     if(num in range(9, 11)):
#         print("in range")
#     else:
#         print("out of range")

# range_num(num)

# num = 5
# def even_or_odd(num):
#     if num%2 == 0:
#         print("even")
#     else:
#         print("odd")

# even_or_odd(num)

# num = 27
# def divisbility_by_3(num):
#     if num%3 == 1:
#         print("it gives 1 as remainder")
#     else:
#         print("it doesn't give 1")

# divisbility_by_3(num)

# num = 3.9
# def is_floating_point(num):
#     if type(num) == float:
#         print("it's float")
#     else:
#         print("it's integer")

# is_floating_point(num)

# mylist = ["apple", "kiwi", "banana", "grape", "orange", "tangerine", "lemon", "lime", "coconut", "tomato"]
# def check_length(mylist):
#     for i in mylist:
#         if len(i) < 6:
#             print(i)

# check_length(mylist)

# mystr = "I really do not like eating apples and bananas"
# def checking_character_a(mystr):
#     count = 0
#     for i in mystr:
#         if i == "a":
#             count += 1
#     print(count)

# checking_character_a(mystr)

# mystr = "I really do not like eating apples and bananas"
# def checking_vowels(mystr):
#     count = 0
#     for i in mystr:
#         if i == "a" or i == "e" or i == "i" or i == "u" or i == "o" or i == "A" or i == "E" or i == "I" or i == "U":
#             count += 1
#     print(count)

# checking_vowels(mystr)

# mystr = "I really do not like eating apples and bananas"
# def reversing_string(mystr):
#     print(mystr[::-1])

# reversing_string(mystr)

# mylist = [12, 4, 5, 9, 15, 0, 98, 6]
# def even_or_odd_sum(mylist):
#     even_sum = 0
#     odd_sum = 0
#     for i in mylist:
#         if i%2 == 0:
#             even_sum += i 
#         else:
#             odd_sum += i
#     print(f"odd sum = {odd_sum}")
#     print(f"even sum = {even_sum}")

# even_or_odd_sum(mylist)

# mystr = "I really do not like eating apples"
# def first_and_last_letter(mystr):
#     print(mystr[0])
#     print(mystr[-1])

# first_and_last_letter(mystr)

# mystr = "I really do not like eating apples"
# def reversed_string(mystr):
#     print(mystr[::-1].capitalize())

# reversed_string(mystr)

# def ab_times_100(a, b):
#    print(a/b*100)

# ab_times_100(65,36)

# mystr = "I really do not like eating apples and bananas"
# def fith_index_s(mystr):
#     if mystr[5] == "s":
#         print("yes")
#     else:
#         print("no")

# fith_index_s(mystr)

# mystr = "I do not like eating apples"
# def length_less_than_6(mystr):
#     if len(mystr) < 6:
#         print("it is less than 6")
#     else:
#         print("it is greater than 6")

# length_less_than_6(mystr)

# mylist = ["apple", "kiwi", "banana", "grape", "orange", "tangerine", "lemon", "lime"]
# def less_than_6(mylist):
#     for i in mylist:
#         if len(i) < 6:
#             print(i)

# less_than_6(mylist)

# mylist = [12, 6, 9, 23, 9, 3, 0, 89, 27, 54, 81, 1]
# def divisble_by_3(mylist):
#     sum = 0
#     for i in mylist:
#         if i % 3 == 0:
#             sum += i 
#     print(sum)

# divisble_by_3(mylist)
# num = 3
# def square(num):
#     print(num**2)

# square(num)

# mylist = [9, 3, 6, 4, 12, 19, 20, 34, 7, 56]
# def multiplication(mylist):
#     product = 1
#     for i in mylist:
#         product *= i
#     print(product)

# multiplication(mylist)

# mystr = "hello"
# num = 5
# def repeat(mystr, num):
#     print(mystr * num)

# repeat(mystr, num)

mylist = [9, 3, 6, 4, 12, 19, 20, 34, 7, 56]
def sum_of_squares(mylist):
    sum = 0
    for i in mylist:
        sum += (i**2)
    print(sum)

sum_of_squares(mylist)