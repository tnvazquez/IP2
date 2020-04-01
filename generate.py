# generate.py
# !/usr/bin/python

"""A Python program generating a list of prime numbers and output them into a csv file
 
"""

from primepackage import *


def main():
    """Generate 100 prime numbers and output it into output.csv file
 
    """
    try:
        primes = getNPrime(100)
        write_primes(primes, 'output.csv')

        l = read_primes('output.csv')
    except IOError:
        print("File cannot be found")
    else:
        print(l)


if __name__ == '__main__':
    main()
