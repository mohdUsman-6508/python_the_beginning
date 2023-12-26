# comments --> write HW of comment  how and why don't write what etc.

# try and except
# exit code 0 --successful , exit code 1 -- code failed

try:
    age = int(input("days>"))
    days = int(input("how many days in a year :"))
    year = age / days
    print(f'Age in years: {year}')
except ValueError:
    print("Invalid Value")
except ZeroDivisionError:
    print("Invalid year")
