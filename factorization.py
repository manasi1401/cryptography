from math import *
import random
from cryptomath import *


def factor(n, m):
    if m == 1:
        return fermats_method(n)
    if m == 2:
        return pollard_rho(n)
    if m == 3:
        return pollard_p_1(n)


print(pollard_rho(295927))
print(fermats_method(295927))
print(pollard_p_1(295927))
print(pollard_p_1(166))
print(pollard_p_1(455927))
print(factor(295927, 1))
print(is_prime(166))
print(is_prime(2441))
# print(is_prime(53471161))
print (is_prime(2024861779763903))
print (is_prime(1100457818531))
print (random_prime(50))
print(modular_sqr_root(2, 71))

print(extendedgcd(5,26))