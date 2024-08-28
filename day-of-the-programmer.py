# This program is under development ******
# Theme - Day of the programmer

year = int(input().strip())
def dayOfProgrammer(year):
    if 1700 <= year <= 1917: # Julian Calender
        if year%4==0:
            # print(f"12.09.{year}")
            return f"12.09.{year}"
        else :
            # print(f"13.09.{year}")
            return f"13.09.{year}"

    elif year == 1918:      # Gregarion Calender
        # print("26.09.1918")
        return "26.09.1918"

    elif year > 1918:       # Gregarion Calender
        if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
            print(f"12.09.{year}")
            return f"12.09.{year}"
        else:
            print(f"13.09.{year}")
            return f"13.09.{year}"
        
dayOfProgrammer(year)

# Need to check leap year
"""
def is_leap(year): 
    leap = False 
    if (year%4 == 0 and year%100 != 0) or (year%400 == 0): 
        return True 
    else: 
        return leap 
year = int(input()) 
print(is_leap(year))
"""

 