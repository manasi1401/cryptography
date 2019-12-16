from math import *
import random


def gcd(x, y):
    """
    Calculate greatest common divisor between two numbers
    :param x: first number
    :param y: second number
    :return: gcd(x,y)
    """
    if x < y:
        gcd(y, x)

    while y != 0:
        x, y = y, x % y

    return x


# ax + by = c
def extendedgcd(a, b):
    """
    Calculated GCD using extended eucledian method
    :param a: first number
    :param b: second number
    :return: egcd(a,b)
    """
    if b == 0:
        return a, 1, 0
    else:
        g, x, y = extendedgcd(b, a % b)
        return g, y, x - (a // b) * y


def findModInverse(a, n):
    """
    Find a^-1 mod n
    :param a: base number
    :param n: number that takes the mod
    :return: a^-1 mod n
    """
    g, x, y = extendedgcd(a, n)

    if g != 1:
        return -1
    else:
        return x % n


def powerModulus(a, d, n):
    """
    Calculate a^d mod n
    :param a: base
    :param d: power
    :param n: number to take a mod with
    :return: a^d mod n
    """
    r = 1
    a = a % n
    while d > 0:
        if d & 1:
            r = (r * a) % n
        d = d >> 1
        a = (a * a) % n
    return r


def is_prime(n):
    """
    Miller Rabin primality test
    :param n: number to be tested
    :return: True or false
    """
    # check its not 1 or even or 3, 5, 7
    if n == 1:
        return False
    if n == 2 or n == 3 or n == 5 or n == 7:
        return True

    if n % 2 == 0:
        return False
    # n-1
    m = n - 1
    k = 0
    while m % 2 == 0:
        k = k + 1
        m = m / 2.0
    # n-1 = 2^k * m
    # Testing multiple times
    for i in range(5):
        if computeMiller(int(m), k, n) is False:
            return False

    return True


def computeMiller(m, k, n):
    """
    perform Millers test to check for Primality
    :param m: m from n-1 = 2^k *m
    :param k: k from n-1 = 2^k *m
    :param n: Number to be tested
    :return:
    """
    a = random.randint(1, n - 1)
    # b = a^m mod n
    b = powerModulus(a, m, n)
    # if b = 1 or -1 mod n then its a prime
    if b == 1 or b == n - 1:
        return True

    # Testing it K time
    while k >= 0:
        # b = b^2 mod n
        b = (b * b) % n
        # b = 1 mod n it is composite
        if b == 1:
            return False
        # b = -1 mod n it is probably a prime
        if b == n - 1:
            return True
        k = k - 1
    return False


def all_primes(n):
    """
    Return all primes in the range 1 to n
    :param n: upper limit of the range
    :return: list of primes till n
    """
    primes = []
    for i in range(1, n):
        if is_prime(i):
            primes.append(i)

    return primes


def random_prime(b):
    """
    random prime of bit string of length b
    :param b: number of bits
    :return: random prime between 2^b-1 and 2^(b+1) -1
    """
    s = 2 ** b - 1
    e = 2 ** (b + 1) - 1

    randNum = random.randint(s, e)
    while is_prime(randNum) is False:
        randNum = random.randint(s, e)

    return randNum


def pollard_rho(n):
    """
    Calculate a factor of n using pollard rho method
    :param n: number to factorized
    :return: factor of n
    """
    if n == 1:  # if no prime divisors for 1
        return n

    if n % 2 == 0:
        return 2

    x = random.randint(2, n)  # range of divisors from 2 to N
    y = x
    c = random.randint(1, n)

    d = 1
    # f(x) = (x^2 +c) mod n
    while d == 1:
        # x = f(x)
        x = ((x * x) % n + c) % n
        # y = f(f(y))
        y = ((y * y) % n + c) % n
        y = ((y * y) % n + c) % n
        d = gcd(abs(x - y), n)
    if d == n:  # no factor found
        return n
    return d


def fermats_method(n):
    """
    Calculate factor of n using Fermat's Method
    :param n: number to factorized
    :return: factor of n
    """
    if is_prime(n):
        return n
    x = ceil(sqrt(n))
    y = x * x - n
    while (int(sqrt(y))) ** 2 != y:
        x = x + 1
        y = x * x - n
    return int(x - sqrt(y))


def pollard_p_1(n):
    """
    Calculate factor of n using Pollards P1 Method
    :param n: number to factorized
    :return: factor of n
    """
    b1 = 1 # lower bound
    b2 = 1000 # upper bound
    # compute all primes less than b2
    primes = all_primes(b2)
    while b1 <= b2:
        a = random.randint(2, n)
        g = gcd(a, n)
        if 1 < g < n:
            return g

        for p in primes:
            # ignore if p is greater than b1
            if p < b1:
                power = 1
                while p * power <= b1:
                    power *= p
                a = powerModulus(a, power, n)
                g = gcd(a - 1, n)
                if 1 < g < n:
                    return g
        b1 = b1 * 2
    return 1



def compute_sqr_root(a, n):
    """
    Helper function to compute square root of a mod n
    :param a: base
    :param n: modular n
    :return: x where x^2 = a mod n
    """
    # p = 3 mod 4
    if n % 4 != 3:
        return 0

    # make sure a < n
    a = a % n
    # x = a ^ (n+1)/4 mod n
    x = powerModulus(a, int((n + 1) / 4), n)
    if (x * x) % n == a:
        return x
    # if x has no roots then -x has roots
    x = n - x
    if (x * x) % n == a:
        return x

    return 0


def modular_sqr_root(a, n):
    """
    Compute square root of a mod n
    :param a: base
    :param n: modular n
    :return: x where x^2 = a mod n
    """
    if is_prime(n):
        x = compute_sqr_root(a, n)
        return x, n - x
    else:
        print("n is not prime")
        return 0
    # if n can be factored

def is_square(n):
    """
    Check if a given number is perfect square
    :param n: number to be checked
    :return: true or false
    """
    rt = floor(sqrt(n))
    rt = int(rt)
    if rt*rt == int(n):
        return True
    else:
        return False


def shanks_Helper(n,k):
    """
    Find factors of n using Shank's Square Form for  multiplier k
    :param n: number to factored
    :param k: multiplier
    :return: Factor of n, 0 if it doesn't exist
    """
    if is_prime(n) or is_square(n):
        return n
    # initialize
    p0 = floor(sqrt(k*n))
    p_prev = p0
    q0 = 1
    q1 = k*n - p0*p0
    p1 = 0
    i = 2
    # loop till Q1 is perfect square
    while is_square(q1) is False:
        temp = q1
        b = floor((p0+p_prev)/q1)
        p1 = b*q1-p_prev
        q1 = q0+b*(p_prev - p1)
        i += 1
        q0 = temp
        p_prev = p1
        if i > sqrt(n):
            break
    # reinitialize
    b = floor((p0-p1)/sqrt(q1))
    p0 = b*sqrt(q1) + p1
    p1 = p_prev = p0
    q0 = sqrt(q1)
    q1 = (k*n - p_prev*p_prev)/q0
    i = 0
    # loop until p1 !=p_prev
    while True:
        b = floor((p0 + p1)/q1)
        p_prev = p1
        temp = q1
        p1 = b*q1 - p1
        q1 = q0 + b * (p_prev - p1)
        i += 1
        q0 = temp
        if p1 == p_prev:
            break
        if i > sqrt(n):
            break
    f = gcd(n, p1)
    f = int(f)
    if f is not 1 and f is not n:
        return f
    return 0


def ShanksSquareForm(n):
    """
    Find factors of n
    :param n: number to factored
    :return: pair of factors of n
    """
    for i in k:
        f = shanks_sq(n,i)
        if f is not 0:
            return f
    return n


def factorize(n, m):
    """
    Lets you choose what method you want to use for factorizing.
    1 - Fermat's Method
    2 - Pollard Rho
    3 - Pollard P-1
    4 - Shank's Form
    :param n:
    :param m:
    :return:
    """
    if m == 1:
        return fermats_method(n)
    if m == 2:
        return pollard_rho(n)
    if m == 3:
        return pollard_p_1(n)
    if m == 4:
        return ShanksSquareForm(n)
