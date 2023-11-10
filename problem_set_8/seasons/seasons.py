'''
In a file called seasons.py, implement a program that prompts the user for their date 
of birth in YYYY-MM-DD format and then sings prints how old they are in minutes, rounded 
to the nearest integer, using English words instead of numerals, just like the song from Rent, 
without any and between words. Since a user might not know the time at which they were born, assume, 
for simplicity, that the user was born at midnight (i.e., 00:00:00) on that date. And assume that the 
current time is also midnight. In other words, even if the user runs the program at noon, assume that 
it’s actually midnight, on the same date. Use datetime.date.today to get today’s date, 
per docs.python.org/3/library/datetime.html#datetime.date.today.
'''
from datetime import date
import inflect
import sys

def validator(dat):
    
    try:
        year, month, day = dat.split("-")
        year = int(year)
        month= int(month)
        day = int(day)
        if not (1 <= day <= 31 and 1<= month <= 12):
           sys.exit("Invalid date") 
        if date(year, month, day) > date.today():
            sys.exit("Invalid date") 
        else:
            return date(year, month, day)
    except ValueError:
        sys.exit("Invalid date")

def comparator(input_date, today):
    diference = (today - input_date).total_seconds()
    diference1 = diference/60
    return int(diference1)

def transform(seconds):
    p = inflect.engine()
    words = p.number_to_words(seconds, andword='')
    
    return f"{words.capitalize()} minutes"

def main():
    print(transform(comparator(validator(input("Date of Birth: ")), date.today())))


if __name__ == "__main__":
    main()