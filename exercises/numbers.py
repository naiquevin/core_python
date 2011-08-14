from math import pi

# 5.2
def calculate_product(a, b):
    return a * b

def show_product(a, b):
    product = calculate_product(a, b)
    print "%r X %r = %r" %(a, b, product)

# 5.3 
class InputError(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return repr(this.msg)

def calculate_grade(score):
    if score > 100:
        raise InputError('Value out of range (0-100)')
    if 100 >= score >= 90:
        return 'A'
    elif 89 >= score >= 80:
        return 'B'
    elif 79 >= score >= 70:
        return 'C'
    elif 69 >= score >= 60:
        return 'D'
    else:
        return 'E'

def do_calculate_grade(score):
    try:
        print calculate_grade(score)
    except InputError as e:
        print "InputError occured, %s" % (e.msg)

# 5.4
def leap_year(year):
    """
    Modulus. Determine whether a given year is a leap year, using the following formula:
    a leap year is one that is divisible by four, but not by one hundred, unless it is also
    divisible by four hundred. For example, 1992, 1996, and 2000 are leap years, but
    1967 and 1900 are not. The next leap year falling on a century is 2400.
    """
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

# 5.5
def denominate(amount):
    """
    Modulus. Calculate the number of basic American coins given a value less than 1
    dollar. A penny is worth 1 cent, a nickel is worth 5 cents, a dime is worth 10 cents,
    and a quarter is worth 25 cents. It takes 100 cents to make 1 dollar. So given an
    amount less than 1 dollar (if using floats, convert to integers for this exercise),
    calculate the number of each type of coin necessary to achieve the amount,
    maximizing the number of larger denomination coins. For example, given $0.76, or 76
    cents, the correct output would be "3 quarters and 1 penny." Output such as "76
    pennies" and "2 quarters, 2 dimes, 1 nickel, and 1 penny" are not acceptable
    """
    if amount > 1.0:
        print "Amount must be less than 1 dollar"
        return None
    cents = int(amount * 100)    
    if cents < 5:
        unit = 'pennies' if cents > 1 else 'penny'
        return '%d %s' % (cents, unit)
    else:
        if cents/100 == 1:
            value = 100
            unit = 'dollar'
        elif cents/25 > 0:
            value = 25
            unit = 'quarter'
        elif cents/10 > 0:
            value = 10
            unit = 'dime'
        elif cents/5 > 0:
            value = 5
            unit = 'nickel'
    parts = cents/value
    r = cents % value
    unit = unit + 's' if parts > 1 else unit
    if r == 0:
        return '%d %s' % (parts, unit)
    else:
        return '%d %s %s' % (parts, unit, denominate(float(r)/100))    

#5.5
def calculator(expression):
    """
    Arithmetic. Create a calculator application. Write code that will take two numbers and
    an operator in the format: N1 OP N2, where N1 and N2 are floating point or integer
    values, and OP is one of the following: +, -, *, /, %, **, representing addition,
    subtraction, multiplication, division, modulus/remainder, and exponentiation,
    respectively, and displays the result of carrying out that operation on the input
    operands. Hint: You may use the string split() method, but you cannot use the exal
    () built-in function
    """
    n1, op, n2 = expression.split(' ')
    n1 = int_or_float(n1)
    n2 = int_or_float(n2)    
    value = 0
    if op == '+':
        value = n1 + n2
    elif op == '-':
        value = n1 - n2
    elif op == '*':
        value = n1 * n2
    elif op == '/':
        value = n1 / n2
    elif op == '%':
        value = n1 % n2
    elif op == '**':
        value = n1 ** n2
    return value

def int_or_float(string):
    try:
        value = int(string)
    except ValueError:
        try:
            value = float(string)
        except ValueError:
            print 'Not an int or float'
    return value

# 5.8
def area_square(side):
    return side ** 2

def area_cube(side):
    return side ** 3

def area_circle(radius):
    return pi * (radius ** 2)

def area_sphere(radius):
    return (3.0/4) * pi * (radius ** 2)

# 5.10
# Conversion. Create a pair of functions to convert Fahrenheit to Celsius temperature
# values. C = (F - 32) * (5 / 9 ) should help you get started. We recommend you try
# true division with this exercise, otherwise take whatever steps are necessary to ensure
# accurate results.

def Fnht_to_Cel(fnht):
    return (fnht - 32) * (5.0 / 9)

def Cel_to_Fnht(cel):
    return (cel * 9.0 / 5.0) + 32

# 5.11
def output_even(maxnum=20):
    nums = [str(i) for i in range(maxnum) if (i%2 == 0)]
    print ", ".join(nums)

def output_odd(maxnum=20):
    nums = [str(i) for i in range(maxnum) if (i%2 == 1)]
    print ", ".join(nums)

# 5.12 todo

# 5.13
def time_to_mins(t):
    """
    Conversion. Write a function that will take a time period measured in hours and
    minutes and return the total time in minutes only
    """
    import re
    match = re.match(r"(\d+)\s+hours\s+(\d+)\s+minutes", t)
    if match is None:
        print "Please provide the input in format - 'h hours m minutes'"
        exit()
    hours, minutes = match.groups()
    return '%d minutes' % ((int(hours) * 60) + int(minutes))
 
if __name__ == '__main__':
    # print Fnht_to_Cel(70)
    # print Cel_to_Fnht(21.1)
    # output_even()
    # output_odd()
    print time_to_mins('3 hours 40 minutes')
    
