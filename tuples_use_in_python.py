# a tuple is a collection which is ordered
# and unchangeable. In python tuples are
# written with round brackets
# example
thistuple = ("apple", "banana", "cherry")
print(thistuple)

# you can access tuple items by
# refering to the index number,
# inside sqaure brackets:
print(thistuple[1])
print(thistuple[0])
print(thistuple[2])

# Negative indexing mean beginning from
# the end, -1 refers to last item, -2 
# refers to the second last item etc.
print(thistuple[-1])
print(thistuple[-2])
print(thistuple[-3])

# you can specify a range of indexes 
# by specifying where to start and where to
# end the range. When specifying a range,
# the return value will be a new tuple
# with the specified items.
thistu = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistu[2:5])
print(thistu[-5:-1])
print(thistu[4:])
print(thistu[:5])
print(thistu[4:5])
print(thistu[:])


# change tuples values
# once a tuple is created, you cannot change its values.
# Tuples are unchangeable, or immutable as it also is called
# but there is a workaround. You can convert the tuple into a 
# list, change the list, and convert the list back into a tuple
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
y[2] = "mango"
x = tuple(y)
print(x)