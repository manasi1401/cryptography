from math import *
from frequency import *


def get_string():
    str = input("Enter string to be encoded: ")
    return str.upper()


def get_key():
    str = input("Enter key: ")
    return str.upper()


def vigenere_encode(str, key):

    cipher = ""
    for i in range(len(str)):
        val = (ord(str[i]) + ord(key[i% len(key)]) - 130) % 26
        cipher += chr(val + 65)

    return cipher


def vigenere_decode(cistr, key):

    orig = ""

    for i in range(len(cistr)):
        val = (ord(cistr[i]) - ord(key[i% len(key)]) + 26) % 26
        orig += chr(val +65)

    return orig

str = get_string()
key = get_key()
cipher = vigenere_encode(str, key)
decipher = vigenere_decode(cipher, key)
frequency = analyze(cipher)
print(cipher)
print(decipher)