import time
from datetime import date
from datetime import time
from datetime import datetime


def main():

    today = date.today()
    print("Today's date is",today)

    print("Today's Weekday#:",today.weekday())

    main()

def supercool():
    i = 1

    while i < 5:
        try:

             print(i)
             i += 10
        except:

             print("That is it folks")


supercool()