# 2D list

matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(len(matrix1))

for row in matrix1:
    for item in row:
        print(item)

# list methods

list1 = [1, 2, 3, 4, 3, 2, 1, 8, 9, 10]

print(list1)
list1.append(11)
print(list1)
print(list1.count(3))

print(list1.index(10))
print(list1.insert(2, 10))
print(list1.pop())
list1.sort()
print(list1)
list1.reverse()
print(list1)

print(list1.remove(4))
list1.clear()
print(list1)

# remove duplicates from list
list2 = [1, 1, 2, 2, 3, 3, 5, 5, 6, 6, 4, 4, 7, 7]

for num in list2:
    if list2.count(num) > 1:
        list2.remove(num)

print(list2)
