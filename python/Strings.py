# strings

# mystr = "Megan"
# print(mystr[2])

# print(mystr[1])

# print(mystr[0])

# print(print[3])

# mystr = "I am having a big task"

# print(mystr[5])
# print(mystr[11])

# we cannot change/update a string's value
# mystr[5] = 'p'

mystr = "I am having a big task"
# #big
# print(mystr[14:17])

# havi
# print(mystr[5:9])

# g a big
# print(mystr[10:17])

# m hav
# print(mystr[3:8])

#avin
# print(mystr[6:10])

# print(mystr[2:5])

# print(mystr[18:])

# print(mystr[0:11])

# if you are not putting any start index, it will be starting from 0 index
# if you are not putting any end index, it will go up to the last element
# print(mystr[:])

# print(mystr[0:5:2])
# print(mystr[2:9:2])
# print(mystr[3:6:2])

# print(mystr[2::2])
# print(mystr[4::4])

# print(mystr[::5])

# print(mystr[-7])
# print(mystr[5])
# print(mystr[-17])

# print(mystr[-5:-2])

# print(mystr[-8:-1:2])
# print(mystr[-5::2])

# print(mystr[-2:-7:-2])

# print(mystr[-8:-7:-2])

# print(mystr[-6:-1:2])

# print(mystr[-4:0:-4])

# print(mystr[-9:1:-3])

# print(mystr[-7:15:-1])

# print(mystr[7:-14])

# Strings Practice

mystring = "Megan studies in first grade"
# print(mystring[2:13])

# print(mystring[-26:-15])

# print(mystring[2:-15])

# print(mystring[-26:13])

# print(mystring[9:22:3])
 
# print(mystring[-19:-6:3])

# print(mystring[9:-6:3])

# print(mystring[-19:22:3])

# print(mystring[-5:-14:-2])

# mystr = "Football is a very famous game"
# print(mystr[2:-12:2])

# print(mystr[15:30:2])

# print(mystr[-15::2])

# print(mystr[15::2])

# print(mystr[-15:30:2])

# print(mystr[-7:-26:-3])

# print(mystr[23:4:-3])

# String Functions

mystring = "Meganlearnspython"

# print(mystring.count("n"))

# print(mystring.index("Urvashi"))

# print(mystring.find("Urvashi"))

# Index and find function both returns lowest index of the substring but index function returns value error 
# and find function returns -1 when the substring is not found.

# print(mystring.isalnum())

# Isalnum checks if a string contains only alphabets or numbers and returns True but if it contains anything
# other than that it contains False

# if mystring.isalnum():
#     print("It is alphamuneric")
# else:
#     print("It is not alphamuneric")

# mystr="I play foorball very often"

# print(mystr.endswith("trn"))

# print(mystr.startswith("play"))


# print(mystr.strip())

# Strip function removes the spaces from the start and end of the string.

# x = mystr.replace("Megan", "Raymond")
# print(x)

# Replace function replaces a particular part of the string with something else.

# print(mystr.isnumeric())

# isnumeric function checks if all the string numeric or not

# print(mystr.isalpha())

# isalpha checks if string contains all the alphabets.
# Spaces are not alphabets. They're symbols.

# print(mystr.count("n"))

# mystr = "    Megan    is  LearNing  pYthoN    "

# print(mystr.capitalize())

# print(mystr.casefold())

# Casefold function converts all the uppercase characters from the string into lowercase

# mystr= "Banana apple mango"

# print(mystr.center(50))

# Center function puts the string in the center and fills the remaining places with spaces

# mystr = "h\te\tl\tl\to"

# print(mystr.expandtabs())

# Expandtabs function converts all the \t present in the string into four spaces

# mystr = "Hello, welcome to my world"
# x = mystr.find("my world")
# print(x)

# Find function returns the starting index of the string which you pass in it

# mystr = "4.2"
# x = mystr.isdecimal()
# print(x)

# isdecimal function checks if the string contains decimal numbers in the place of all the characters

# mystr = "for"
# x = mystr.isidentifier()
# print(x)

# There is difference between a variable and an identifier that vaiable should follow all ther variable naming conventions
# but identifier can conatin reserved keywords

# mystr = "Hello there"
# x = mystr.isprintable()
# print(x)

# isprintable function checks if a string prints exactly the same as it is written or not

mystr = "Python is a programing language"

words = mystr.split("is")
print(words)

mystr = mystr.lower()
print(mystr)
