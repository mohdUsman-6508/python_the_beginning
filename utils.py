def maximum(list):
    max = list[0]
    for num in list:
        if max < num:
            max = num

    return max


def total_bill(cart):
    sum = 0
    for item in cart:
        sum += item
    return sum
