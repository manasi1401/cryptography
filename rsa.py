#################################################
# Author: Manasi Paste
# Course: Cryptography
# Professor: Dr. Karlsson
#
# Description: This program demonstrates, Key Generation, encryption
# and decryption using RSA cipher
# Requirements: Numpy, Math and Matplotlib library
#
# Run instructions: python rsa.py
#################################################
from cryptomath import *
import random


def generate_keypair():
    """
    Generate P and Q random prime. N =PQ. Compute e and d such that
    a = (a^e)^d mod n
    :return: e, n, d
    """
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


def encrypt_rsa(publicK, plaintext):
    """
    Encrypt every single charachter in the plaintext using RSA
    cipher = message^e mod n
    :param publicK: public key (e, n)
    :param plaintext: input string
    :return: cipher
    """
    e, n = publicK
    # make it uppercase
    plaintext = plaintext.upper()
    cipher = []
    for ch in plaintext:
        c = powerModulus(ord(ch), e, n)
        cipher.append(c)
    return cipher


def decrypt_rsa(privateK, cipher):
    """
    Decrypt the cipher using private key in RSA
    message = cipher ^d mod n
    :param privateK: Private key of the user
    :param cipher: Cipher to be decrypted
    :return: plaintext
    """
    d, n = privateK
    plain = ""
    for ch in cipher:
        c = powerModulus(ch, d, n)
        plain = plain + str(chr(c))

    return plain


def main():
    e, n, d = generate_keypair()
    print("e: ", e, "n: ",n, "d: ", d)
    message = input("Enter a message: ")
    cipher = encrypt_rsa([e, n], message)
    print("Cipher: ", cipher)
    print("Decrypted Message: ", decrypt_rsa([d, n], cipher))

if __name__== "__main__":
  main()
