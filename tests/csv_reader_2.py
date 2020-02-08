import csv
import subprocess
from config_globals import *

## Directory Locations
framework_directory = ROOT_DIR
config_file_directory = CONFIG_PATH
test_case_directory = framework_directory / 'utilities' / 'test_cases'
screenshot_directory = framework_directory / 'test_results' / 'screenshots'

test_case = "test_login_Chrome"

csv_directory = str(test_case_directory / test_case) + ".csv"

with open(csv_directory) as f:
    rows = list(csv.reader(f))
    username = rows[1][1]
    print(username)
    password = rows[1][2]
    print(password)
    env = rows[1][3]
    print(env)

# with open(test_case_directory+'test_login_Chrome.csv') as f:
#     rows = list(csv.reader(f))
#     username = rows[1][1]
#     print(username)
#     password = rows[1][2]
#     print(password)
#     env = rows[1][3]
#     print(env)


# with open('test_login_Chrome_01.csv') as f:
#     f_csv = csv.reader(f)
#     # Skip the header
#     headers = next(f_csv)
#     for row in f_csv:
#         username = row[1]
#         password = row[2]
#         env = row[3]