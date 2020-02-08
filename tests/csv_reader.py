import csv

with open("test_login_Chrome_01.csv", 'r') as csvfile:
    reader = csv.reader(csvfile)

    for row in reader:
        print(row)

csvfile.close()