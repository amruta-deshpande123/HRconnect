import csv
from datetime import datetime
from utils.csv_ import HandleCSV
"""
Write a program to get "HIRE DATE" of employee who's department is within range 30
to 110 AND who's salary is > 4200.
The output should be in following format.

"""
getdata = []

data=HandleCSV.read_entire_csv()

for lines in data:

    if 30 < int(lines['DEPARTMENT_ID']) < 110 and int(lines['SALARY']) > 4200:
        date = datetime.strptime(lines['HIRE_DATE'] , "%d-%b-%y")
        date = date.strftime("%Y-%d-%m")
        print(date)
        getdata.append({date : lines['FIRST_NAME'] + " " + lines['LAST_NAME']})

for employee in getdata:
    print(employee)