from math import *
from cryptomath import *
import numpy as np

#  0:A 1:D 2:F 3:G 4:X
adfgx = ["A", "D", "F", "G", "X"]

#  size of matrix 5x5
alphaMatrix = "pgcenbqozrslaftmdviwkuyxh"


def encrypt(pt, key):
    # string to store substitution cipher
    subs_cipher = ""
    # convert it lower case
    pt = pt.lower()

    for i in range(len(pt)):
        # calculate row by dividing by 5
        r = floor(alphaMatrix.index(pt[i])/5)
        # calculating col by modulus 5
        c = alphaMatrix.index(pt[i]) % 5
        subs_cipher += adfgx[r] + adfgx[c]

    # if not even then add X
    if len(subs_cipher) % 2 != 0:
        subs_cipher += "X"

    keyLen = len(key)
    # sort just the indexes
    sortedKey = sorted(range(keyLen), key = lambda i: key[i])
    s = len(subs_cipher)
    # string to store cipher text
    cipher = ""
    for i in sortedKey:
        for j in range(i, s, keyLen):
            cipher += subs_cipher[j]

    return cipher


def decrypt(cipher, key):
    keyLen = len(key)
    # sort just the indexes
    sortedKey = sorted(range(keyLen), key=lambda i: key[i])

    # store indexes actual values before sorting
    s = len(cipher)
    x = []
    # calculate index values before sorting
    for i in sortedKey:
        for j in range(i, s, keyLen):
            x.append(j)

    # create a list of size of cipher
    subs = list(cipher)
    # match the actual index to the cipher value
    for i in range(len(x)):
        subs[x[i]] = cipher[i]

    message = ""
    for i in range(0, s, 2):
        r = subs[i]
        c = subs[i+1]
        # find the message from alphaMatrix
        message += alphaMatrix[keyLen*adfgx.index(r) + adfgx.index(c)]
    return message


cipher = encrypt("kaiserWilhelm", "RHEIN")
print("cipher = ", cipher)
d = decrypt(cipher, "RHEIN")
print("decrypted = ", d)