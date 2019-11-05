from math import *


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


