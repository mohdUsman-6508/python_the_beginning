# modules --> we use modules to organize our code

import utils  # this will import all the methods in utils
from utils import total_bill  # this will import specific function

pay = total_bill([2, 3, 5, 3, 2, 4, 5, 1])
print(pay)

max = utils.maximum([1, 2, 13, 4, 5])
print(max)

