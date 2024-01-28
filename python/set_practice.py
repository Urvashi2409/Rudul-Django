myset1 = {1, 4, 5, 1, 1, 2, 4, 6, 7}
myset2 = {3, 4, 4, 5, 9, 10, 3}

myset3 = myset1.symmetric_difference(myset2)
print(myset3)

myset1.update(myset2)
print(myset1)

myset3 = myset1.intersection(myset2)
print(myset3)

print(myset1.isdisjoint(myset2))

myset1.intersection_update(myset2)
print(myset1)

myset3 = myset1.union(myset2)
print(myset3)

mylist = [1, 5, 11, 8, 6, 32, 0, 13]
myset1.update(mylist)
print(myset1)

# myset = {1, "red", 0, "hi", 45, "purple"}

# for i in myset:
#     print(i)

# myset.add(8)
# print(myset)

# myset.remove("red")
# print(myset)

# myset1 = {1, 2, 3}
# myset2 = {3, 4, 5}

# myset3 = myset1.union(myset2)
# print(myset3)

# myset = {"a", "b", "c"}
# myset1 = {"x", "y", "z"}

# print(myset.isdisjoint(myset1))

# myset = {1, 3, 5, 7}
# print(5 in myset)

# myset = {1, 2, 3, 4}
# square_set = set()
# for i in myset:
#     square_set.add(i**2)
# print(square_set)

myset = {1, "red", 0, "hi", 45, "purple"}

# myset.clear()
# print(myset)

# print(len(myset))