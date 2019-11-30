from math import *
import random
from cryptomath import *


def pollard_rho(n):

    if (n ==1): # if no prime divisors for 1
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
        return -1
    return d


def fermats_method(n):
    if is_prime(n):
        return -1
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
    return -1

print(pollard_rho( 295927))
print(fermats_method(295927))
print(pollard_p_1(295927))
print(is_prime(4211))
print(is_prime(166))
print(is_prime(2441))
print(is_prime(53471161))
