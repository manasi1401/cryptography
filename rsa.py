from cryptomath import *
import random


def generate_keypair():
    p = random_prime(10)
    q = random_prime(10)
    # make sure p and q are not same
    while p == q:
        q = random_prime(10)
    # n = pq
    n = p*q
    # phi(n) = p-1*q-1
    phi = (p-1)*(q-1)

    # choosing e
    e = random.randint(1, phi)
    while gcd(e, phi) != 1:
        e = random.randint(1, phi)

    # finding modular inverse of for private key
    d = findModInverse(e, phi)
    # return e, n , d
    return e, n, d


def encrypt(publicK, plaintext):
    e, n = publicK
    # make it uppercase
    plaintext = plaintext.upper()
    cipher = []
    for ch in plaintext:
        c = powerModulus(ord(ch), e, n)
        cipher.append(c)
    return cipher


def decrypt(privateK, cipher):
    d, n = privateK

    plain = ""
    for ch in cipher:
        c = powerModulus(ch, d, n)
        plain = plain + str(chr(c))

    return plain

e, n, d = generate_keypair()
print(e, n, d)
cipher = encrypt([e, n], "Jonnyhadal i8ttleemap")
print(decrypt([d, n], cipher))