# This script calculates the prime numbers no larger than an upper bound,
# which is provided as an integer argument. The primes are written to a file,
# one on each line. The output filename is also provided as an argument.

import argparse
from math import floor, sqrt


# This is the function that calculates and outputs the prime numbers.
def calc_primes(max_prime):
    """ Calculate and print primes at most as large as max_prime. Assumes max_prime is
    at least 7.
    :param max_prime: int
    :return: list of int
    """
    # Initialize the list to hold the primes
    primes = [2, 3, 5]
    # Loop through the numbers in the form of 7 + 6n up to max_prime
    for num in range(7, max_prime + 1, 6):
        # Screen out all numbers that when divided by 6 provide a remainder other than 1 or 5
        if is_prime(num, primes):
            primes.append(num)
        if is_prime(num + 4, primes):
            primes.append(num + 4)
    # Remove last element of primes list if that exceeds the upper bound
    if primes[-1] > max_prime:
        primes.pop()
    return primes


def is_prime(num, primes):
    """ Returns True if num is prime.
    :param num: int
    :param primes: list of int
    :return: boolean
    """
    prime_bound = floor(sqrt(num))
    for p in primes:
        if p > prime_bound:
            break
        if not(num % p):
            return False
    return True


def writePrimes(primes, out_file_name):
    """ Create output file and write primes into it each one on a separate line.
    :param priems: list
    :param out_file_name: file
    :return: None
    """
    with open(out_file_name, "w") as oFile:
        for p in primes:
            oFile.write("{}\n".format(p))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--outputfile", help="output file name", default="primes.txt")
    parser.add_argument("-m", "--max_prime", type=int, help="upper bound of primes", default=22)
    args = parser.parse_args()
    max_prime, out_file_name = args.max_prime, args.outputfile
    primes = calc_primes(int(max_prime))
    # Create output file and write primes into it
    writePrimes(primes, out_file_name)
    # print(len(primes))
