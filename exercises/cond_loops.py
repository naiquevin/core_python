#!/usr/bin/env python

# 8.4
def is_prime(n):
    """
    Prime Numbers. We presented some code in this chapter to determine a number's
    largest factor or if it is prime. Turn this code into a Boolean function called isprime()
    such that the input is a single value, and the result returned is true if the number is
    prime and False otherwise.
    """
    if n == 1:
        return False
    f = n/2
    while f > 1:
        # print f
        if n%f == 0:
            return  False
            break
        f -= 1        
    else:
        return True

# 8.5
def getfactors(n):
    """
    Factors. Write a function called getfactors() that takes a single integer as an
    argument and returns a list of all its factors, including 1 and itself.
    """
    return [x for x in range(1,n+1) if n%x == 0]

# 8.6
def get_prime_factors(n):
    """
    Prime Factorization. Take your solutions for isprime() and getfactors() in the
    previous problems and create a function that takes an integer as input and returns a
    list of its prime factors. This process, known as prime factorization, should output a
    list of factors such that if multiplied together, they will result in the original number.
    Note that there could be repeats in the list. So if you gave an input of 20, the output
    would be [2, 2, 5].
    """
    f = [x for x in getfactors(n) if is_prime(x) or x == 1]
    while True:
        m = reduce(lambda x, y: x*y, f)
        # print f, n, m
    	q = n/m
        if q == 1:
            break
        else:
            f.extend(get_prime_factors(q))
    return sorted(f)

# 8.7
def isperfect(n):
    """
    Perfect Numbers. A perfect number is one whose factors (except itself) sum to itself.
    For example, the factors of 6 are 1, 2, 3, and 6. Since 1 + 2 + 3 is 6, it (6) is
    considered a perfect number. Write a function called isperfect() which takes a single
    integer input and outputs 1 if the number is perfect and 0 otherwise.
    """
    factors = filter(lambda x: x != n, getfactors(n))
    if sum(factors) == n:
        return 1
    else:
        return 0

if __name__ == '__main__':
    # print is_prime(227)
    # print getfactors(31)
    # print get_prime_factors(17)
    # print isperfect(28) # others 6, 496
    pass        
