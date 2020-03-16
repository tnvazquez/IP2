# primeio.py
import csv
""" This function writes a list of prime numbers to a csv file. 
    Input Arguments: List of prime number and csv file name. 
    """

def write_primes(l, file_name):
    with open('file_name', 'w', newline='') as file:
        prime = csv.writer(file)
        for row in file_name:
            prime.writerow(row)


""" This function reads prime numbers from a csv file and save them into a list. 
    Input Arguments: csv file.
    Return: A list of prime numbers
"""

def read_primes(file_name):
    prime_list = []
    with open('file_name', 'r') as file:
        read_prime = csv.reader(file)
        for i in read_prime:
            prime_list.append(i)
            return prime_list
