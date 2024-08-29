"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeInWords' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER m
#

def timeInWords(h, m):
    # Write your code here
    #********* IZHAR CODE **********
    translate_hour = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve']
    translate_minute = ['', 'one minute', 'two minutes', 'three minutes', 'four minutes', 'five minutes', 'six minutes', 'seven minutes', 'eight minutes', 'nine minutes', 'ten minutes', 'eleven minutes', 'twelve minutes', 'thirteen minutes', 'fourteen minutes', 'quarter', 'sixteen minutes', 'seventeen minutes', 'eighteen minutes', 'nineteen minutes', 'twenty minutes', 'twenty one minutes', 'twenty two minutes', 'twenty three minutes', 'twenty four minutes', 'twenty five minutes', 'twenty six minutes', 'twenty seven minutes', 'twenty eight minutes', 'twenty nine minutes', 'half']
    if m <= 30:
        connection = " past "
    else:
        connection = " to "
    h = (h + m//31) % 13 + (h + m//31)//13
    m = 30 - abs(30-m)
    if m == 0:
        return translate_hour[h]+" o' clock"
    return translate_minute[m] + connection + translate_hour[h]

    #************* IZHAR CODE *****************

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input().strip())

    m = int(input().strip())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()

"""

#********* Logic Working fine *******
"""
def timeInWords(h, m):
    # Write your code here
    translate_hour = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve']
    translate_minute = ['', 'one minute', 'two minutes', 'three minutes', 'four minutes', 'five minutes', 'six minutes', 'seven minutes', 'eight minutes', 'nine minutes', 'ten minutes', 'eleven minutes', 'twelve minutes', 'thirteen minutes', 'fourteen minutes', 'quarter', 'sixteen minutes', 'seventeen minutes', 'eighteen minutes', 'nineteen minutes', 'twenty minutes', 'twenty one minutes', 'twenty two minutes', 'twenty three minutes', 'twenty four minutes', 'twenty five minutes', 'twenty six minutes', 'twenty seven minutes', 'twenty eight minutes', 'twenty nine minutes', 'half']
    if m <= 30:
        connection = " past "
    else:
        connection = " to "
    h = (h + m//31) % 13 + (h + m//31)//13
    m = 30 - abs(30-m)
    if m == 0:
        return translate_hour[h]+" o' clock"
    return translate_minute[m] + connection + translate_hour[h]
""" 


#********* Logic-2 But no  clearing testcase 2(of 3) *****************
"""
h = int(input().strip())
m = int(input().strip())
def timeInWords(h, m):
    
    num_words = {
        1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 
        6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", 
        11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 
        15: "quarter", 16: "sixteen", 17: "seventeen", 18: "eighteen", 
        19: "nineteen", 20: "twenty", 21: "twenty one", 22: "twenty two", 
        23: "twenty three", 24: "twenty four", 25: "twenty five", 
        26: "twenty six", 27: "twenty seven", 28: "twenty eight", 
        29: "twenty nine", 30: "half"
    }
    
    if m == 0:
        # return f"{num_words[h]} o'clock"
        print(f"{num_words[h]} o'clock")
    elif m <= 30:
        if m == 15 or m == 30:
            # return f"{num_words[m]} past {num_words[h]}"
            print(f"{num_words[m]} past {num_words[h]}")
        else:
            # return f"{num_words[m]} minute{'s' if m > 1 else ''} past {num_words[h]}"
            print(f"{num_words[m]} minute{'s' if m > 1 else ''} past {num_words[h]}")
    else:
        next_hour = h + 1 if h < 12 else 1
        if m == 45:
            # return f"quarter to {num_words[next_hour]}"
            print(f"quarter to {num_words[next_hour]}")
        else:
            # return f"{num_words[60 - m]} minute{'s' if (60 - m) > 1 else ''} to {num_words[next_hour]}"
            print(f"{num_words[60 - m]} minute{'s' if (60 - m) > 1 else ''} to {num_words[next_hour]}")


timeInWords(h, m)
"""


#********* Logic-3 But no  clearing testcase 2(of 3) *****************
"""
def number_to_words(number):
    number_word_dictionary = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'quarter',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
        20: 'twenty',
        21: 'twenty one',
        22: 'twenty two',
        23: 'twenty three',
        24: 'twenty four',
        25: 'twenty five',
        26: 'twenty six',
        27: 'twenty seven',
        28: 'twenty eight',
        29: 'twenty nine',
        30: 'half'
        
    }
    
    return number_word_dictionary[number]


def timeInWords(h, m):
    if m > 30:
        hours = number_to_words(h + 1)
        minutes = number_to_words(60 - m)
        past_or_to = 'to'
    elif m > 0:
        hours = number_to_words(h)
        minutes = number_to_words(m)
        past_or_to = 'past'
    else:
        hours = number_to_words(h)
        return hours + ' ' + "o' clock"
    if m == 1:
        return minutes + ' minute ' + past_or_to + ' ' + hours
    if m == 15 or m == 30 or m == 45:
        return minutes + ' ' + past_or_to + ' ' + hours
    else:
        return minutes + ' minutes ' + past_or_to + ' ' + hours
        
"""
