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
    return s[::-1]

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
    
    
if __name__ == '__main__':
    # print is_palindrome('abca')
    pass
