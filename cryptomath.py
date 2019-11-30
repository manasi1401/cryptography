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


def pollard_rho(n):

    if (n == 1): # if no prime divisors for 1
        return n

    if n % 2 == 0:
        return 2

    x = random.randint(2, n) # range of divisors from 2 to N
    y = x
    c = random.randint(1, n)

    d = 1 # divisor
    # f(x) = (x^2 +c) mod n
    while d == 1:
        x = ((x*x) % n + c) % n
        y = ((y*y) % n + c) % n
        y = ((y*y) % n + c) % n
        d = gcd(abs(x-y), n)
    if d == n: # no factor found
        return n
    return d


def fermats_method(n):
    if is_prime(n):
        return n
    a = ceil(sqrt(n))
    b2 = a*a - n
    while (int(sqrt(b2)))**2 != b2:
        a = a + 1
        b2 = a*a - n
    return int(a - sqrt(b2))


def pollard_p_1(n): # needs to be worked on
    b1 = 100
    a = 2
    for i in range(b1):
        a = powerModulus(a, i, n)
        g = gcd(a - 1, n)
        if 1 < g < n:
            return g
    return n


def compute_sqr_root(a,n):
    # p = 3 mod 4
    if n % 4 != 3:
        return 0

    # make sure a < n
    a = a % n
    # x = y ^ (p+1)/4 mod n
    x = powerModulus(a, int((n+1)/4), n)
    if (x*x) % n == a:
        return x
    # if y has no roots then -y has roots
    x = n - x
    if (x*x) % n == a:
        return x

    return 0


def modular_sqr_root(a, n):

    if is_prime(n):
        x = compute_sqr_root(a, n)
        return x, n - x
    # if n can be factored
