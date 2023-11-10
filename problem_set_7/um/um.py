'''
It’s not uncommon, in English, at least, to say “um” when trying to, um, think of a word. 
The more you do it, though, the more noticeable it tends to be!

In a file called um.py, implement a function called count that expects a line of text as 
input as a str and returns, as an int, the number of times that “um” appears in that text, 
case-insensitively, as a word unto itself, not as a substring of some other word. For instance, 
given text like hello, um, world, the function should return 1. Given text like yummy, though, 
the function should return 0.

Structure um.py as follows, wherein you’re welcome to modify main and/or implement other functions 
as you see fit, but you may not import any other libraries. You’re welcome, but not required, 
to use re and/or sys.
'''
import re

def main():
    print(count(input("Text: ")))


def count(s):
   num = re.findall(r"\bum\b", s, re.IGNORECASE) 
   cont = len(num)
   return cont


if __name__ == "__main__":
    main()