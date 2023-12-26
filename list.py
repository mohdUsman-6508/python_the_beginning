# lists [item1,item2,.....] it has 0 based indexing , it also has negative index

num = [-1, 2, -3, 4, -5, -4, 3, -2, 1]
max = num[0]
min = num[0]
for number in num:
    if max < number:
        max = number
    if number < min:
        min = number
print(f'''Maximum number: {max}
Minimum number: {min}''')

