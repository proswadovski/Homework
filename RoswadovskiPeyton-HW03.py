# Name: Peyton Roswadovski

# Lab Section: 14

# Submission Date: 11/05/24

# Sources, help given to/received from: Friend/former student in class
#  Didn't have time to learn to finish the end

def leap_year(year):
    if (year % 4 == 0):
        return True
    elif ((year % 100 == 0) or (year % 400 != 0)):
        return False

def day_of_jan_1st(year):
    y = year - 1
    day = (36 + y + (y // 4) - (y // 100) + (y // 400)) % 7
    return day

def valid_date(month, day, year):
    if month < 1 or month > 12:
        return False
    days_in_month = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }
    if leap_year(year):
        days_in_month[2] = 29 

    if day < 1 or day > days_in_month.get(month, 0):
        return False
    return True

def day_of_week(month, day, year):
    first_day_of_year = day_of_jan_1st(year)
    
    days_in_month = [
        31, 28, 31, 30, 31, 30,
        31, 31, 30, 31, 30, 31
    ]
    
    if leap_year(year):
        days_in_month[1] = 29 

    total_days = sum(days_in_month[:month-1]) + (day - 1)

    day_of_week = (first_day_of_year + total_days) % 7
    return day_of_week

date_input = input("Enter a date in the format (MMDDYYYY): ")
weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

# Overview

# Your goal for this program is to write a program that given a date of the format MM/DD/YYYY, your program will then
# state the day of the week the date occurs on.

# Notes

# April, June, September, November have 30 days

# January, March, May, July, August, October, December have 31 days

# February typically has 28 days, 29 in a leap year

# Leap years occur in years equally divisible by 4, and not by 100 except in the case when they are
# divisible by 400. So 2000 was a leap year, however 2100 will not be

# Assume that Sunday is day 0 with Saturday being day 6

# The day of the week that January 1st falls on can be determined using the following equation:

# let y = year -1
# Jan first falls on day x where:
# day = (36 + y +(y/4) - (y/100) + (y/400))%7

# This equation uses integer division rounded down

# Once this is found, you can find what day of the week all other dates fall on. Your program should check for
# invalid input. Make sure you are checking if it is a leap year if 2/29/XXXX is entered for example, and that
# none of the other dates are going out of bounds. If the input is not valid, the dates supplied don’t work, etc
# alert the user to the issue.

# Input

# Your code should accept input from the command line. Dates in the form of MM/DD/YYYY will be inputted.

# Output

# Your code should output the inputted date followed by the day of the week it falls on, or that is invalid:

# 02/21/2022 Monday

# 01/01/2022 Saturday

# 02/29/2024 Thursday

# 02/29/2023 Invalid Date

# 04/31/2023 Invalid Date

# 02/00/2023 Invalid Date

# Hints

# Here are some suggestions, they aren't required but they will make your life easier:

# Break things down into functions, such as:
# Checking if it is a leap year
# Calculating on what day January 1st occurs
# Checking if the date entered is valid
# Calculating the day of the week for the supplied date
# Utilize data structures!
# This helps make your code more concise
# And also is easier to program
# A dictionary to map months with their days
# A list for days of the week
# etc
# // is Python's floor division
# Meaning, it will divide two numbers and give you the integer result rounded down
# 9//2 would give 4 for example
# Have a calendar open when testing this
# Test edge cases
# leap days in leap years and not
# Days after a leap day
# Going out of bounds in a month
# etc
# DISALLOWED

# You CANNOT use external libraries to determine the day of the week something occurs on, e.g the DateTime library. Doing so will result in your program receiving a 0. You must write all the solution yourself.

# Submission

# Submit your file named as: LastnameFirstName-HW03.py

# Your python file must include the standard required comments at the top of your file.

#

