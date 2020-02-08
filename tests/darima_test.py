default = 'x'
selected_value = 'y'

if len(selected_value) > 0:
    print("selected value is Not null, using selected value of " + selected_value)
    print("end program")
else:
    print("selected value is null. using default value of " + default)
    print("end program")