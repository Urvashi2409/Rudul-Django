# mytuple = (3, 4, "b", True, "banana")
# print(mytuple[2])

# mytuple[2] = 19
# print(mytuple)

# mylist = [3, 4, "b", True, "banana"]
# print(mylist[2])

# mylist[2] = 19
# print(mylist)

# You can change the value of a list but not a tuple
# List is mutable and tuples are immutable

# print(len(mytuple))

# mytuple = (34)
# print(type(mytuple))

# mytuple = ("hi",)
# print(type(mytuple))

# A single element tuple is not a tuple while it has a comma after element

# mylist = ["green", 5, "banana", 6, 19, 12, "orange"]
# print(type(mylist))

# mytuple = tuple(mylist)
# print(type(mytuple))

# Tuple() is a constructor which is used to convert list into tuple
# Both negitive and positive indexing work for tuples also
# List slicing also works in tuple
# All the operators work the same way in tuples as in the list
# For loop in tuples works same way as in list

# Append function is not in tuple because we cannot add a new value in tuples
# append, insert function is not there in tuples as we cannot add a value in tuples
# remove, pop functions do not work in tuples as we cannot delete a value from tuple.
# del mytuple[2] doesn't work in tuple as we cannot delete a value from tuple.
# we need to come back on a topic(packing and unpacking of tuples)

mytuple = (9, "lily", "plum", 3, 6, "blue")

# for i in mytuple:
#     print(i)

print(mytuple[1:3])

# You cannot update tuple


# Backing and Unpacking of Tuple

mytuple = (3, "cucumber", 9)

