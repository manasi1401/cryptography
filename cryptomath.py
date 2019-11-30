from math import *
import random


def gcd(x, y):
    if x < y:
        gcd(y, x)

    while y != 0:
        x, y = y, x % y

    return x


# ax + by = c
def extendedgcd( a, b):

    if b == 0:
        return a, 1, 0
    else:
        g, x, y = extendedgcd(b, a % b)
        return g, y, x - (a//b)*y


def findModInverse(a, n):
    g, x, y = extendedgcd(a, n)

    if g != 1:
        return -1
    else:
        return x % n


def powerModulus(a, d, n):
    r = 1
    a = a % n
    while d > 0:
        if d & 1:
            r = (r*a) % n
        d = d >> 1
        a = (a*a) % n
    return r

def is_prime(n):
    """
    Miller Rabin primality test
    :param n: number to be tested
    :return: True or false
    """
    if n ==1:
        return False
    if n == 2 or n == 3 or n ==5 or n ==7:
        return True

    if n % 2 == 0:
        return False

    d = n - 1
    while d % 2 == 0:
        d = d/2.0
    for i in range(3):
        if computeMiller(int(d), n) is False:
            return False

    return True

def computeMiller(d, n):
    a = random.randint(2, n)
    x = powerModulus(a, d, n)

    if x == 1 or x == n - 1:
        return True

    while d != n - 1:
        x = (x * x) % n
        d = d * 2
        if x == 1:
            return False
        if x == n - 1:
            return True
    return False


def all_primes(n):
    primes = []
    for i in range(1, n):
        if is_prime(i):
            primes.append(i)

    return primes


def random_prime(b):
    s = 2**b-1
    e = 2**(b+1) -1

    randNum = random.randint(s, e)
    while is_prime(randNum) is False:
        randNum = random.randint(s, e)

    return randNum




