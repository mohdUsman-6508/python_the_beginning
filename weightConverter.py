unit = input("Select unit: kg/lbs ")
weight = int(input(f'Enter weight({unit}) :'))

if unit == 'kg':
    print(f'Weight(lbs) :{2.24 * weight}')
else:
    print(f'Weight(kg) :{0.453 * weight}')
