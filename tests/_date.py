from datetime import datetime
from utilities.date_time_generator.date_time_generator import date_time_generator
from utilities.date_validator.date_validator import date_validator

# Create Instance of Date Time Generator
dtg = date_time_generator()
# Create Today's Date
date_today = dtg.return_date_today()
date_one_month_ago = dtg.return_date_one_month_ago()
test_date_2 = datetime(2019, 1, 1, 1)

# print(date_today)
# print(date_today.weekday())

dt = date_validator()
valid_date = dt.return_valid_date(date_one_month_ago)
formatted_valid_date = dtg.format_and_return_date(valid_date)

print(valid_date)
print(formatted_valid_date)
print("end program")
