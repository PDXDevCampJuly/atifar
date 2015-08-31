# This script calculates the prime factorization of a command line integer argument,
# The factorizaton is then printed.

import argparse

from pre_assignment_stuff import primes


def factor(number):
    """ This function decomposes its argument into its prime factors. It prints
    a string representing the factorization in the following format:
    "number = prime1[^ord1] * prime2[^ord2] * ..."
    :param number:
    :return: None
    """
    # Save argument for output string
    num_to_factor = str(number)
    # Generate a list of primes
    prime_list = primes.calc_primes(number)
    # Create an empty dictionary to hold the prime factors
    factors = {}
    # As long as the number to factor is not a prime, ...
    while number not in prime_list:
        # ... then whichever prime divides it, ...
        for prime in prime_list:
            if number % prime == 0:
                # ... increment the count value for that prime in factors, or
                # set count to 1 for the first occurrence of the prime in factors
                factors[prime] = factors.get(prime, 0) + 1
                # Divide number by its identified prime factor and continue factoring.
                number //= prime
                break
    # If number is a prime, add it to factors
    factors[number] = factors.get(number, 0) + 1
    # Build output string
    factor_list = sorted(factors.items())
    factorization = [str(prm) if ord == 1 else str(prm) + "^" + str(ord) for prm, ord in factor_list]
    print(num_to_factor + " = " + "*".join(factorization))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--number", type=int, help="number to factor", default=60)
    args = parser.parse_args()
    number = args.number
    factor(number)
