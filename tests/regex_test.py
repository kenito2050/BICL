import re
import time

account_number = "55838600"
Name = "David J Martin CTDN"
Total = "63.92"
Phone = "(619) 569-5797"
bus_phone = "(619) 283-3107"
rep_code = "KS03"

regex= "\(\w{3}\)\w{3}-\w{4}"
regex_1 = "(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})"

# r1 = re.findall(r"^\w+",account_number)
# print(r1)
#
# r2 = re.findall(r"^\w+",Name)
# print(r2)
#
# r3 = re.findall(r"^\w+",Total)
# print(r3)
#
# r6 = re.findall(r"^\w+",rep_code)
# print(r6)

if re.search(regex_1, Phone):
    print("phone number found")
else:
    print("phone number not found")

if re.search(regex_1, bus_phone):
    print("phone number found")
else:
    print("phone number not found")

time.sleep(1)