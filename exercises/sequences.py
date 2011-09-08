#!/usr/bin/env python

import string
import keyword
from random import choice
from numbers import leap_year

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

# 6.14        
class Rochambeau(object):
    """
    *Random Numbers. Design a "rock, paper, scissors" game, sometimes called
    "Rochambeau," a game you may have played as a kid. Here are the rules. At the same
    time, using specified hand motions, both you and your opponent have to pick from
    one of the following: rock, paper, or scissors. The winner is determined by these rules,
    which form somewhat of a fun paradox:
    a.
    the paper covers the rock,
    b.
    the rock breaks the scissors,
    c.
    the scissors cut the paper. In your computerized version, the user enters his/
    her guess, the computer randomly chooses, and your program should indicate
    a winner or draw/tie. Note: The most algorithmic solutions use the fewest
    number of if statements.
    """

    weapons = ["rock", "paper", "scissors"]
    
    @staticmethod
    def runner():
    	user_choice = None
    	while user_choice not in Rochambeau.weapons:
    	    if user_choice is not None:
    	        print "Sorry you can't choose that. Please enter a correct one now. okay!!"
    	    user_choice = raw_input("Choose your weapon from among rock, paper or scissors ? > ")
    	computer_choice = choice(Rochambeau.weapons)
        roch = Rochambeau()
        result = roch.find_winner(user_choice, computer_choice)
    	print "Computer chose %s" % computer_choice
    	print "You chose %s" % user_choice
        print result
        again = raw_input("Play again ? (y/n) > ")
    	if again == 'y':
    	    Rochambeau.runner()
    	else:
    	    print "Okay. It was nice playing with you!!"
    	    exit(1)

    def find_winner(self, user_choice, computer_choice):
        result = 'computer wins!!'
        user_power = Rochambeau.weapons.index(user_choice)
        computer_power = Rochambeau.weapons.index(computer_choice)
    	# print user_power, computer_power
    	if user_power == computer_power:
    	    result = 'its a draw!!'
    	elif user_power - computer_power in [1, -2]:
    	    result = 'you win!!'
        return result    

# 6.15
class DateConvertor(object):
    """
    Conversion.
    a.
    Given a pair of dates in some recognizable standard format such as MM/DD/YY
    or DD/MM/YY, determine the total number of days that fall between both dates.
    b.
    Given a person's birth date, determine the total number of days that person
    has been alive, including all leap days.
    c.
    Armed with the same information from (b) above, determine the number of
    days remaining until that person's next birthday.
    """
    months = [
        (1, 31),
        # feb will be inserted dynamically depending upon leap year
        (3, 31),
        (4, 30),
        (5, 31),
        (6, 30),
        (7, 31),
        (8, 31),
        (9, 30),
        (10, 31),
        (11, 30),
        (12, 31)
        ]

    def __init__(self, d1, d2):
        self.d1 = tuple([int(x) for x in d1.split('/')])
        self.d2 = tuple([int(x) for x in d2.split('/')])

    def days_between(self):
        days  = DateConvertor.days_upto_year_end(*self.d1)
        days += sum((366 if leap_year(y) else 365) for y in range(self.d1[2]+1, self.d2[2]))
        days += DateConvertor.days_from_year_start(*self.d2)
        return days
    
    @staticmethod
    def days_upto_year_end(day, month, year):
        # copy months list twice and set the correct number of days for feb
        months = DateConvertor.months[:]
        months[1:1] = [(2, 29)] if leap_year(year) else [(2, 28)]
        days = months[month-1][1] - day
        rem_months = months[month:]
        days += sum(int(n) for m, n in rem_months)
        return days

    @staticmethod
    def days_from_year_start(day, month, year):
        # copy months list twice and set the correct number of days for feb
        months = DateConvertor.months[:]
        months[1:1] = [(2, 29)] if leap_year(year) else [(2, 28)]
        prev_months = months[:month-1]
        days = day + sum(int(n) for m, n in prev_months)
        return days

# 6.1 Matrices. Process the addition and multiplication of a pair of M by N matrices.
class Matrix(object):
    @staticmethod
    def add(m1, m2):
        """
    	Matrix Addition
    	"""    	
    	# rows
    	r1 = len(m1)
    	r2 = len(m2)
    	# columns
    	c1 = len(m1[0])
    	c2 = len(m2[0])
    	if r1 != r2 or c1 != c2:
    	    print "Only matrices of the same order can be added"
    	    exit(1)
    	m3 = []
    	for i in range(len(m1)):
    	    # print i, m1[i], m2[i]
    	    a = []
    	    for j in range(len(m1[i])):
    	        a.append(m1[i][j] + m2[i][j])
    	    m3.append(a)
    	return tuple([tuple(s) for s in m3])

    @staticmethod
    def multiply(m1, m2):
        # rows
    	r1 = len(m1)
    	r2 = len(m2)
    	# columns
    	c1 = len(m1[0])
    	c2 = len(m2[0])
    	if c1 != r2:
    	    print "Invalid matrices"
    	    exit(1)
        m3 = []
        for i in range(r1):
            a = []
            for j in range(c2):
                s = 0
                for k in range(r2):
                    s += m1[i][k]*m2[k][j]
                a.append(s)
            m3.append(a)
    	return tuple([tuple(s) for s in m3])
    
    
if __name__ == '__main__':
    # print is_palindrome('abca')
    # Rochambeau.runner()
    pass
    

