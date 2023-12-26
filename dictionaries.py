student = {
    "name": 'osman',
    "subject": 'engineering',
    "institute": 'AMU',
}

print(student['name'])
student['hobby'] = 'programming'
print(student)

numbers = {
    "1": 'one ',
    '2': 'two ',
    '3': 'three ',
    '4': 'four ',
    '5': 'five ',
    '6': 'six ',
    '7': 'seven ',
    '8': 'eight ',
    '9': 'nine ',
    '0': 'zero '
}

num = 786
word = ''
for n in str(num):
    word += numbers[n]

print(word)
