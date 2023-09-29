"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    x = 2
    while len(list) < number_of_primes:
        if ifprime(x):
            list.append(x)
        x = x+1
    return list

def ifprime(num):
    for i in range(2,num): # for all possible factors of i
        if num % i == 0: # if it is a factor
            return False
    return True