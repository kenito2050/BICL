import math
from decimal import Decimal




num_1 = str(1.55)
num_2 = str(1.222)
num_3 = str(1.0)
num_4 = str(1)

num_decimal_places = num_4[::-1].find('.')
print(num_decimal_places)
if num_decimal_places == 2:
    print("PASS")
else:
    print("FAIL")


# is_decimal = False
# if ( (int)(value * 100.0) % 100 == 0 ):
#     is_decimal = True
#     print("Decimal")
# else:
#     print("Not A Decimal")