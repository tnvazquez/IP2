# primemodule.py

import math
""" Determine if a number is prime or not. 
    
    Arguments: 
        n (integer): Natural number
    
    Return: 
        Boolean: True if n is prime, false if not.
    Raises:
        Exception if n is not greater than 0
"""
def isPrime(n):
    if n <= 0:
        raise ValueError("Value must be greater than 0")
    if n > 0:
        if n == 2:
            return True
        for i in range(2, n):
            if (n % i) == 0:
                return False
        return True

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

