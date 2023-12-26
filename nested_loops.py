# nested loops
# generating all combinations of two dice

for d1 in range(1, 7):
    for d2 in range(1, 7):
        print(f'{d1, d2}')

f = [5, 2, 5, 2, 2]
for char in f:
    print(char * 'x')

f = [5, 2, 2, 2, 5]
for char in f:
    if char == 5:
        print(char * 'x')
    else:
        print(char * ' x')

f = [2, 2, 2, 2, 5]

for i in f:
    str = ''
    for j in range(i):
        str += 'X'
    print(str)
