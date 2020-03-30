 #primeio.py
import csv


def write_primes(l, file_name):

    """ This function writes a list of prime numbers to a csv file.
    Arguments:
        l = list of prime numbers
        file_name (str): csv file name
    Raise:
        IO error if file cannot be found.
    """
    try:
        with open(file_name, "w") as file:
            prime = csv.writer(file)
            for row in range(len(l)):
                prime.writerow([l[row]])
    except IOError:
        print("Numbers cannot be written into file")


def read_primes(file_name):
    """ This function reads prime numbers from a csv file and save them into a list.
    Arguments:
        file_name (str): csv file.
    Return:
        list: a list of prime numbers.
    Raise:
        IOError: io error.

"""

    try:
        prime_list = []
        with open(file_name, "r") as file:
            read_prime = csv.reader(file)
            for i in read_prime:
                prime_list.append(i)
    except IOError:
        print("File cannot be found or file cannot be opened")
    else:
        return prime_list

