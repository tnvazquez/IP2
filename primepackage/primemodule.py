# primemodule.py

import math
""" Determine if a number is prime or not. 
    Arguments: 
    n (integer): Natural number
    Return: 
    Boolean: True if n is prime, false if not.
"""
def isPrime(n):
    if n > 1:
        for i in range(2, int(math.sqrt(n))+1):
            if (n % i) == 0:
                return True

            return False

    return False
def getNPrime(num):
    """ Generates a list of prime numbers. Amount of numbers is given in parameter.
        Arguments:
             num (integer): Integer Number
        Return:
            list: List of prime numbers
    """
    prime_numbers = []
    for i in range(num):
        if isPrime(i + 1):
            prime_numbers.append(i)
        return prime_numbers

