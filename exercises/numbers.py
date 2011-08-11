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
 
if __name__ == '__main__':
    print denominate(0.79)
    
# 5.8 
