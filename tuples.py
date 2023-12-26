# tuples --> these are pretty much like list but what made them unique is
#            that they are immutable i.e. we cannot add, remove or modify any value in the tuple

tuple1 = (10, 5, 18)
print(tuple1)

# UNPACKING --> a concept in python which is used to unpack list item more easily
# it is productive method

coordinates = (108, 12, 9)
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]
print(x * y * z // 9)
# this above hard work of typing can be done in smart way by using unpacking
# - unpacking in action
a, b, c = coordinates
print(a * b * c // 9)
