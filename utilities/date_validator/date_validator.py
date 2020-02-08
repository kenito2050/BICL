from datetime import datetime, timedelta
import holidays

### Purpose:
### To return a date that is NOT on a holiday or on a Saturday or Sunday (Weekend)
### If Date is on a Holiday or Weekend, then a new date value will be selected until a valid date (no holiday
### or weekend date is selected

class date_validator:

    def return_valid_date(self, inputdate):

        N1 = 1
        N2 = 2

        # January 1 -- New Years Day
        test_date_2 = datetime(2019, 1, 1, 1)

        ### Test Module
        original_date_value = test_date_2
        original_date_value_formatted = original_date_value.strftime('%Y-%m-%d')

        # declare us_holidays variable
        us_holidays = holidays.UnitedStates()

        # January 1 -- New Years Day
        # inputdate = test_date_2

        valid = False

        while not valid:
            # this checks if inputdate is a holiday
            is_date_a_holiday = (inputdate in us_holidays)
            if is_date_a_holiday:
                print(inputdate)
                print("Date fell on a Holiday. New Date of " + str(inputdate - timedelta(days=N1)) + " picked")
                inputdate = inputdate - timedelta(days=N1)

            # next part guarantees inputdate is a weekday
            elif inputdate.weekday() == 6:
                print(inputdate)
                print("Date fell on a Sunday. New Date of " + str(inputdate - timedelta(days=N2)) + " picked")
                inputdate = inputdate - timedelta(days=N2)
            elif inputdate.weekday() == 5:
                print(inputdate)
                print("Date fell on a Saturday. New Date of " + str(inputdate - timedelta(days=N1)) + " picked")
                inputdate = inputdate - timedelta(days=N1)
            else:
                valid = True
                print("Date " + str(inputdate) + " is valid and does not fall on a Holiday, Sunday or Saturday")

        return inputdate