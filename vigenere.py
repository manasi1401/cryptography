from math import *
from frequency import *


def get_string():
    """
    Get string as an input
    :return: string converted to upper case
    """
    str = input("Enter string to be encoded: ")
    return str.upper()


def get_key():
    """
    Get the key from the user
    :return: key converted to upper case
    """
    str = input("Enter key: ")
    return str.upper()


def vigenere_encode(str, key):
    """
    To encode using vigenere algorithm add each character from
    the plain text to the corresponding character from the key.
    :param str: string to be encoded
    :param key: key to be used for encoding
    :return: encrypted cipher
    """
    cipher = ""
    for i in range(len(str)):
        val = (ord(str[i]) + ord(key[i% len(key)]) - 130) % 26
        cipher += chr(val + 65)

    return cipher


def vigenere_decode(cistr, key):
    """
    To decode subtract every character from the cipher with
    the corresponding character from the key
    :param cistr:cipher string
    :param key: key to be used to decode
    :return: original message
    """
    orig = ""

    for i in range(len(cistr)):
        val = (ord(cistr[i]) - ord(key[i% len(key)]) + 26) % 26
        orig += chr(val +65)

    return orig



def main():
    str = get_string()
    key = get_key()
    cipher = vigenere_encode(str, key)
    decipher = vigenere_decode(cipher, key)
    frequency = analyze(cipher)
    print(cipher)
    print(decipher)

if __name__== "__main__":
  main()