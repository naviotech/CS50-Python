'''
In the United States, dates are typically formatted in month-day-year order (MM/DD/YYYY), 
otherwise known as middle-endian order, which is arguably bad design. Dates in that format can’t 
be easily sorted because the date’s year comes last instead of first. Try sorting, for instance, 
2/2/1800, 3/3/1900, and 1/1/2000 chronologically in any program (e.g., a spreadsheet). Dates in that 
format are also ambiguous. Harvard was founded on September 8, 1636, but 9/8/1636 could also be 
interpreted as August 9, 1636!

Fortunately, computers tend to use ISO 8601, an international standard that prescribes that dates 
should be formatted in year-month-day (YYYY-MM-DD) order, no matter the country, formatting years 
with four digits, months with two digits, and days with two digits, “padding” each with leading 
zeroes as needed.

In a file called outdated.py, implement a program that prompts the user for a date, anno Domini, 
in month-day-year order, formatted like 9/8/1636 or September 8, 1636, wherein the month in the 
latter might be any of the values in the list below:

[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
Then output that same date in YYYY-MM-DD format. If the user’s input is not a valid date in either 
format, prompt the user again. Assume that every month has no more than 31 days; no need to validate 
whether a month has 28, 29, 30, or 31 days.
'''

def application_number():

    while True:
        list=["January","February","March","April","May","June","July","August","September","October","November","December"]

        date = input("Introducing your date in format numeral month/day/year or an expample September 8, 1636\n")
        if "/" in date:
            try:
                month, day, year = date.split("/")
                year= int(year)
                month= int(month)
                day = int(day)
            except ValueError:
                continue
            if 0 < int(month) <= 12 and 0< int(day) <= 31:
                print(f"{year:04d}-{month:02d}-{day:02d}")
                break
            else:
                print("Your date it's wrong, try again")
        if "," in date:
            month, day, year = date.title().split(" ")

            if month in list:
                month1 = list.index(month)
                month2 = int(month1)
                month3 = month2 + 1
                month4 = str(month3)
                day1 = day.replace(",","")
                day2 = day1.replace(" ","")
                year1 = year.replace(" ","")
                year1 = int(year1)
                month4 = int(month4)
                day2 = int(day2)

                if 0 < int(month4) <= 12 and 0< int(day2) <= 31:
                    print(f"{year1:04d}-{month4:02d}-{day2:02d}")
                    break
                else:
                    print("Your date it's wrong, try again")
                    continue
        else:
            continue


application_number()