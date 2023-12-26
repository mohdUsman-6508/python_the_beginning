# for loop  range function

for char in 'osman':
    print(char)

for item in ['apple', 'orange', 'mango', 'grapes', 'papaya']:
    print(item)

for num in range(10):
    print(num)

for num in range(11, 21):
    print(num)

for num in range(1, 10, 2):
    print(num)
# ///////////////////////////////////////////////////////////////////////

sum = 0
for item_price in [100, 120, 20, 30, 40, 10, 50, 80, 12]:
    sum += item_price

print(f'Total price to pay is: {sum} Rs')
