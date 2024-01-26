# inporting the modules needed
import calendar
from datetime import date
from months import months_dict, months_dict_index


# print loading state
def load():
    for i in range(2):
        print("..................................")


load()
print()
print("This program take your birth date in the format YEAR-MM-DD")
print()
name = input("What's Your name: ")
print()
load()

print()
birth_date = input(f"When were you born {name.title()} (YEAR-MM-DD): ").split("-")
birth_date = [int(item) for item in birth_date]
year, month, day = birth_date


# Get current date
def current_date():
    current_date = str(date.today()).split("-")
    current_year, current_month, current_day = current_date
    return int(current_year), int(current_month), int(current_day)


# calculating user age
def user_age(year, month):
    current_year, current_month, current_day = current_date()
    if current_month >= month:
        return current_year - year
    else:
        return current_year - 1 - year


# calculating next age
def birthday(year, month, day):
    age = user_age(year, month)
    c_date = current_date()
    c_month = c_date[1]
    if c_month < month:
        age += 1
    year += age
    bday = [day, calendar.month_name[month], year]
    bday = [str(item) for item in bday]
    birth_day = " ".join(bday)
    return birth_day


# checking if year is a leap year
def is_leap(year):
    return calendar.isleap(year)


# calculating days from the beginning of the year to the specified day and month
def calc_days(day, b_month):
    c_date = current_date()
    days = 0
    for month in months_dict:
        if months_dict_index[month] < b_month:
            if is_leap(c_date[0]) and month == "February":
                months_dict[month] = 29
                days += months_dict[month]
            else:
                days += months_dict[month]
    return days + day


# calculating days till next birthday
days_till_birthday = calc_days(day, month)
today_date = current_date()
days_used = calc_days(today_date[2], today_date[1])
days_left_to_birthday = days_till_birthday - days_used

# determining the suffix at the end of age
age = str(user_age(year, month))
int_age = int(age[len(age) - 1])
if int_age == 1:
    age += "st"
elif int_age == 2:
    age += "nd"
elif int_age == 3:
    age += "rd"
elif 4 <= int_age <= 9 or int_age == 0:
    age += "th"

# printing result to user
print()
load()
print()
birth_day = birthday(year, month, day)

print(f"{name}, your {age} birthday is in {days_left_to_birthday} days, on {birth_day}")
