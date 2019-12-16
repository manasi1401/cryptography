from math import *
from cryptomath import *
from frequency import *
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
    """
    Encrypt givenplain text using affine cipher
    :param a: a from ax+b mod n
    :param b: b from ax+b mod n
    :param pt: plain text to be encrypted (no whites space or anyother char the 26 letters
    :param n: 26
    :return:
    """
    cipher = ""
    for c in pt:
        ci = (a*(ord(c) - 65)+b) % n
        cipher += str(chr(ci + 65))
    return cipher


def decrypt(a, b, ct, n):
    """
    Decrypt given cipher using Affine Cipher
    :param a: a from a^-1(x-b) mod n
    :param b: b from a^-1(x-b) mod n
    :param ct: cipher to be decrypteed
    :param n: 26
    :return: decrypted message
    """
    a_inv = findModInverse(a, n)
    decipherd = ""
    for c in ct:
        pi = (a_inv*((ord(c)- 65) - b)) % n
        decipherd += str(chr(pi + 65))
    return decipherd


def attack_affine(e, t, n):
    e_cipher = ord(e) - 65
    t_cipher = ord(t) - 65
    # a (4) + b = e_cipher
    # a(19) + b = t_cipher
    # a = (e-cipher - t_cipher)/(-15)
    a = (e_cipher - t_cipher)/(-15.0)
    a = int(a) % n
    while a < 0:
        a += n
    b = (e_cipher - 4*a)%n
    return a, b

def brute_force(cipher, n):
    possible_a = []
    possible_b = range(1, n)
    for i in range(1, n):
        if gcd(i,n)==1:
            possible_a.append(i)
    for i in possible_a:
        for j in possible_b:
            print(decrypt(i, j, cipher, n))


#freq = analyze(xi)
#e, t = print_analysis(freq)
#a1, b1 = attack_affine(e, t, 26)
#attck = decrypt(a1, b1, xi, 26)
#brute_force(xi, 26)

def main():
    a, b = get_ab()
    pt = get_plaintext()
    print("a inverse: ", findModInverse(a,26))
    xi = encrypt(a, b, pt, 26)
    pi = decrypt(a, b, xi, 26)
    print(xi)
    print(pi)


if __name__== "__main__":
  main()