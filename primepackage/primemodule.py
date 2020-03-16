# primemodule.py
""" Determine if a number is prime or not. 
    Input Arguments: Natual number
    Return: Boolean. True if prime, false if not.
"""
import math
def isPrime(n):
    if n > 1:
        for i in range(2, int(math.sqrt(n))+1):
            if (n % i) == 0:
                return True

            return False

    return False


""" Generates a list of prime numbers. Amount of numbers is given in parameter.
    Input Arguments: Integer Number
    Return: List of prime numbers
"""
def getNPrime(num):
    prime_numbers = []

    for i in range(0, num):

        if isPrime(i):
            prime_numbers.append(i)
            return prime_numbers
