#!/usr/bin/env python

import string
import keyword

# 6.3 a
def sort_numlist_desc(li):
    "Enter a list of numbers and sort the values in largest-to-smallest order."
    li.sort(reverse=True)
    return li

# 6.3 b
def sort_string_desc(s):
    """
    Do the same thing, but for strings and in reverse alphabetical (largest-to-
    smallest lexicographic) order.
    """
    return "".join(sorted(s, reverse=True))

# 6.2
def idcheck(identifier):
    """
    String Identifiers. Modify the idcheck.py script in Example 6-1 such that it will
    determine the validity of identifiers of length 1 as well as be able to detect if an
    identifier is a keyword. For the latter part of the exercise, you may use the keyword
    module (specifically the keyword.kwlist list) to aid in your cause.
    """
    alphas = string.letters + '_'
    nums = string.digits
    if len(identifier) > 0:
        if keyword.iskeyword(identifier):
            return False
        elif identifier[0] not in alphas:
            return False
        elif len(identifier) == 1:
            return True
        else:            
            for otherChar in identifier[1:]:
                if otherChar not in alphas + nums:
                    return False
                else:
                    return True

# 6.5 b
def string_cmp(string1, string2):
    """
    Determine if two strings match (without using comparison operators or the cmp
    () built-in function) by scanning each string. Extra credit: Add case-
    insensitivity to your solution.
    """
    string1 = string1.lower()
    string2 = string2.lower()
    for i, s in enumerate(string1):
        if string2[i] != s:
            return False
    return True

# 6.5 c
def is_palindrome(string):
    """
    Determine if a string is palindromic (the same backward as it is forward). Extra
    credit: Add code to suppress symbols and whitespace if you want to process
    anything other than strict palindromes.
    """
    if len(string) in [0, 1]:
        return True
    else:        
        first = string[0]
        last = string[-1]
        if first != last:
            return False
        else:
            return is_palindrome(string[1:-1])
# 6.5 d
def make_palindrome(string):
    """
    Take a string and append a backward copy of that string, making a palindrome.    
    """
    return string + string[::-1]

# 6.6
def mimic_strip(string):
    """
    Strings. Create the equivalent to string.strip(): Take a string and remove all leading
    and trailing whitespace. (Use of string.*strip() defeats the purpose of this exercise.)
    """
    n = len(string)
    i = 0
    j = -1
    new_string = ''
    while i < n and string[i] == ' ':
        i = i+1
    new_string = string[i:]
    if len(new_string) == 0:
        return new_string
    while new_string[j] == ' ':
        j = j-1
    new_string = new_string[:j+1] # since i started with -1
    return new_string

# 6.8
def textify_numbers(num):
    """
    Lists. Given an integer value, return a string with the equivalent English text of each
    digit. For example, an input of 89 results in "eight-nine" being returned. Extra credit:
    Return English text with proper usage, i.e., "eighty-nine." For this part of the exercise,
    restrict values to be between 0 and 1,000.
    """
    if num > 1000 or num < 0:
        print "Please give an input between 0-1000"
        exit(1)
    map = {
        '0': 'zero',
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine'        
        }
    num_str = str(num)
    return "-".join([map[k] for k in num_str])

# 6.9
def minutes_to_hours(minutes):
    """
    Conversion. Create a sister function to your solution for Exercise 5.13 to take the total
    number of minutes and return the same time interval in hours and minutes,
    maximizing on the total number of hours.
    """
    h, m = minutes/60, minutes%60
    text_hours, text_minutes = 'hour' if h == 1 else 'hours', 'minute' if m == 1 else 'minutes'
    return '%d %s and %d %s' % (h, text_hours, m, text_minutes)
    
    
if __name__ == '__main__':
    # print is_palindrome('abca')
    pass
