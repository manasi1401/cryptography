from math import *


def gcd(x, y):
    if x < y:
        gcd(y, x)

    while y != 0:
        x, y = y, x % y

    return x

print(gcd(48, 60))

# ax + by = c
def extendedgcd( a, b):

    if b == 0:
        return a, 1, 0
    else:
        g, x, y = extendedgcd(b, a % b)
        return g, y, x - (a//b)*y


print(extendedgcd(26, 15))

def findModInverse(a, n):
    g, x, y = extendedgcd(a, n)

    if g != 1:
        return -1
    else:
        return x % n

print(findModInverse(3, 11))
print(findModInverse(10, 17))

