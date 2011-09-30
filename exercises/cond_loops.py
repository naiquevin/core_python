#!/usr/bin/env python
import string

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

def factorial(n):
    """
    Factorial. The factorial of a number is defined as the product of all values from one to
    that number. A shorthand for N factorial is N! where N! == factorial(N) == 1 * 2 * 3
    * ... * (N-2) * (N-1) * N. So 4! == 1 * 2 * 3 * 4. Write a routine such that given N, the
    value N! is returned.
    """
    return 1 if n == 1 else n * factorial(n-1)

def fibonacci(n):
    """
    Fibonacci Numbers. The Fibonacci number sequence is 1, 1, 2, 3, 5, 8, 13, 21, etc. In
    other words, the next value of the sequence is the sum of the previous two values in
    the sequence. Write a routine that, given N, displays the value of the Nth Fibonacci
    number. For example, the first Fibonacci number is 1, the 6th is 8, and so on.
    """
    c = 0
    f = [1]
    while c < n-1:
        c_1 = f[-1]
        c_2 = 0 if len(f) <= 1 else f[-2]        
        f.append(c_1 + c_2)
        c += 1
    return f[-1]

# 8.10
def text_processor(sentence):
    """
    Text Processing. Determine the total number of vowels, consonants, and words
    (separated by spaces) in a text sentence. Ignore special cases for vowels and
    consonants such as "h," "y," "qu," etc. Extra credit: create code to handle those
    special case.
    """
    v = ['a', 'e', 'i', 'o', 'u']
    words = sentence.split(" ")
    vowels = [s for s in sentence if s in v]
    c = [s for s in list(string.letters) if s not in v]
    consonants = [s for s in "".join(words) if s in c]
    result = {
        "words": len(words),
        "vowels": len(vowels),
        "consonants": len(consonants)
        }
    return result

if __name__ == '__main__':
    # print is_prime(227)
    # print getfactors(31)
    # print get_prime_factors(17)
    # print isperfect(28) # others 6, 496
    # print factorial(5)
    # print fibonacci(6)
    print text_processor(text_processor.__doc__)
    pass        
