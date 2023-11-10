'''
Whereas most countries use a 24-hour clock, the United States tends to use a 12-hour clock. 
Accordingly, instead of “09:00 to 17:00”, many Americans would say they work “9:00 AM to 5:00 PM” 
(or “9 AM to 5 PM”), wherein “AM” is an abbreviation for “ante meridiem” and “PM” is an abbreviation 
for “post meridiem”, wherein “meridiem” means midday (i.e., noon).

Conversion Table
In a file called working.py, implement a function called convert that expects a str in either of 
the 12-hour formats below and returns the corresponding str in 24-hour format (i.e., 9:00 to 17:00). 
Expect that AM and PM will be capitalized (with no periods therein) and that there will be a space 
before each. Assume that these times are representative of actual times, not necessarily 9:00 AM and 
5:00 PM specifically.

9:00 AM to 5:00 PM
9 AM to 5 PM
Raise a ValueError instead if the input to convert is not in either of those formats or if either 
time is invalid (e.g., 12:60 AM, 13:00 PM, etc.). But do not assume that someone’s hours will start 
ante meridiem and end post meridiem; someone might work late and even long hours 
(e.g., 5:00 PM to 9:00 AM).

Structure working.py as follows, wherein you’re welcome to modify main and/or implement other 
functions as you see fit, but you may not import any other libraries. You’re welcome, but not 
required, to use re and/or sys.
'''
import re

def main():
    print(convert(input("Hours: ").strip()))

def convert(s):
   
    if time:= re.search(r"^([0-1]?[0-2]|[0]?[0-9])(:[0-5][0-9])? \b(AM|PM)\b to ([0-1]?[0-2]|[0]?[0-9])(:[0-5][0-9])? \b(AM|PM)\b$", s):
        first_h, first_min, first_d, second_h, second_min, second_d = time.groups()
        first_min = int(first_min[1:]) if first_min else 0
        second_min = int(second_min[1:]) if second_min else 0
        first_h, first_min, second_h, second_min = map(int,[first_h, first_min, second_h, second_min])
        
        if first_d == "PM" and first_h != 12:
            first_h += 12
        elif first_d == "AM" and first_h == 12:
            first_h = 0

        if second_d == "PM" and second_h != 12:
            second_h += 12
        elif second_d == "AM" and second_h == 12:
            second_h = 0
    
        return f"{first_h:02}:{first_min:02} to {second_h:02}:{second_min:02}"
    else:
        raise ValueError("wrong arguments")


if __name__ == "__main__":
    main()
