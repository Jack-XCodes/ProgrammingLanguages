#  Adjust your Simple calculator app to a version that takes the year of birth of a person and
# # calculates their age in years, months and days respectively. Your app should give all three
# # output
# Import the datetime module to work with dates
from datetime import datetime

# Get the current date
current_date = datetime.now()

# Prompt the user for their birth year, month, and day
birth_year = int(input("Enter your birth year: "))
birth_month = int(input("Enter your birth month: "))
birth_day = int(input("Enter your birth day: "))

# Calculate the difference in years, months, and days
years = current_date.year - birth_year
months = current_date.month - birth_month
days = current_date.day - birth_day

# Adjust for negative values in months and days
if days < 0:
    months -= 1
    days += 30  # Assuming each month has 30 days

if months < 0:
    years -= 1
    months += 12

# Display the age
print(f"Your age is: {years} years, {months} months, and {days} days.")
