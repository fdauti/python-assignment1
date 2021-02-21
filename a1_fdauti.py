#!/usr/bin/env python3
''' The purpose of this program is to take as input data, a date of birth, 
    convert it in a specific format and display the result in standard output.
    The program will accept user input in the following formats, 
    (YYYYMMDD, YYYY/MM/DD, YYYY-MM-DD, or YYYY.MM.DD)
    The result should be displayed on standard output in the "mmm d, yyyy" format. 
-----------------------------------------------------------------------
OPS435 Assignment 1 - Winter 2021
Program: a1_fdauti.py 
Author: "Fatjon Dauti"
The python code in this file (a1_fdauti.py) is original work written by
"Fatjon Dauti". No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.
'''
import os
import sys

def leap_year(obj):
    '''
    Check to see if the year entered by the user is a leap year.
    '''
    # Leap year algorithm 
    # if (year is not divisible by 4) then (it is a common year)
    # else if (year is not divisible by 100) then (it is a leap year)
    # else if (year is not divisible by 400) then (it is a common year)
    # else (it is a leap year)
    
    status = True
    if (obj % 4) != 0:
        status = False
    elif (obj % 100) != 0:
        status = True
    elif (obj % 400) != 0:
        status = False

    return status

def sanitize(obj1,obj2):
    '''
    Remove all the non-digits characters ‘/’, ‘-’, ‘.’ from the user's input data, 
    to extract the year, month, and day.
    '''
    results = ''
    for char in obj1:
        if char in obj2:
            results += char 
    return results

def size_check(obj, intobj):
    '''
    Check if the length of the sanitized user input is 8 characters.
    '''
    status = False
    if len(obj) == intobj:
        status = True
    return status

def range_check(obj1, obj2):
    '''
    Validate the correct range for the year, month and day variables. 
    Return a boolean variable depending of the status of the validation
    '''
    status = False
    r_min = obj2[0]
    r_max = obj2[1]
    if r_min <= obj1 <= r_max:
        status = True
    return status
    
def usage():    
    ''' 
    Remind the user how to use the script to input data in the correct format, 
    if something other than a single command line arguemnt is entered.
    '''
    status = "Usage: a1_fdauti.py YYYYMMDD|YYYY/MM/DD|YYYY-MM-DD|YYYY.MM.DD"
    return status

if __name__ == "__main__":
   # step 1
   if len(sys.argv) != 2:
      print(usage())
      sys.exit()
   # step 2
   month_name = ['Jan','Feb','Mar','Apr','May','Jun',
                 'Jul','Aug','Sep','Oct','Nov','Dec']
   days_in_month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30,
                    7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
   user_raw_data = sys.argv[1]
   # step 3
   allow_chars = '0123456789'
   dob = sanitize(user_raw_data, allow_chars)
   #print('Sanitized user data:', dob)
   # setp 4
   result = size_check(dob,8)
   if result == False:
       print("Error 09: wrong date entered")
       sys.exit()
   # step 5
   year = int(dob[0:4])
   month = int(dob[4:6])
   day = int(dob[6:])
   # step 6
   result = range_check(year,(1900,9999))
   if result == False:
       print("Error 10: year out of range, must be 1900 or later")
       sys.exit()
   result = range_check(month,(1,12))
   if result == False:
       print("Error 02: Wrong month entered")
       sys.exit()
   result = leap_year(year)
   if result == True:
       days_in_month[2] = 29
   result = range_check(day, (1, days_in_month[month]))
   if result == False:
       print("Error 03: wrong day entered")
       sys.exit()
   # step 7
   new_dob = str(month_name[month - 1])+' '+ str(day)+', '+str(year)
   # step 8
   print("Your date of birth is:", new_dob)  