from math import *
from gcd import *
# [A..Z]
N = 26


def get_ab():
    x = input("Enter value of a: ")
    y = input("Enter value of b: ")
    a = int(x)
    b = int(y)

    return a, b


def get_plaintext():
    str = input("Enter plain text: ")
    return str.upper()


def get_ciphertext():
    str = input("Enter cipher text: ")
    return str.upper()


def get_choice():
    c = input("Enter 1 to encrypt or 2 to decrypt: ")
    choice = int(c)
    if choice != 2 and choice != 1:
        c = input("Input can only be 1 or 2, Please reenter your choice: ")
        choice = int(c)
    return choice


def encrypt(a, b, pt, n):
    cipher = ""
    for c in pt:
        ci = (a*(ord(c) - 65)+b) % n
        cipher += str(chr(ci + 65))
    return cipher


def decrypt(a, b, ct, n):
    a_inv = findModInverse(a, n)
    decipherd = ""
    for c in ct:
        pi = (a_inv*((ord(c) - 65) - b)) % n
        decipherd += str(chr(pi + 65))
    return decipherd

