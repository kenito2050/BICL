from datetime import datetime
from datetime import timedelta

# Declare Date / Time Objects

# Sets Today's Date in format dd/mm/YYYY
checkin_date = datetime.now().strftime("%d-%m-%Y")
print (checkin_date)

# Using Today's Date, Adds 7 Days
checkout_date = datetime.now() + timedelta(days=7)
print(checkout_date)

# Format's checkout date in format dd/mm/YYYY
checkout_date_new_format = checkout_date.strftime("%d-%m-%Y")
print (checkout_date_new_format)