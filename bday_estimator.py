# TODO
# If user input year print print age else print only days left to next birthday and day of birthday

# inporting the modules needed
import calendar
from datetime import date

print("Loading.................")
print("This program take your birth date in the format YEAR-MM-DD or MM-DD")
print()
name = input("What's Your name: ")
print(".............................")

birth_date = input(f"When were you born {name.title()}: ").split("-")

# Check whether the user supply year or not
if len(birth_date) == 2:
    month, day = birth_date
elif len(birth_date) == 3:
    year, month, day = birth_date


# Get current date
def current_date():
    current_date = str(date.today()).split("-")
    current_year, current_month, current_day = current_date
    return int(current_year), int(current_month), int(current_day)


# calculating user age
def user_age(year, month):
    current_year, current_month, current_day = current_date()
    if current_month >= int(month):
        return current_year - int(year)
    else:
        return current_year - 1 - int(year)


print(user_age(year, month))
