#################################################
# Author: Manasi Paste
# Course: Cryptography
# Professor: Dr. Karlsson
#
# Description: This program demonstrates encryption
# and decryption using 64 bit DES block cipher.
#
# Run instructions: python des64.py
#################################################
# Permutation Tables from the Cryptography Table
IP = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 29, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7]

IPinv = [40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31,
         38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29,
         36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27,
         34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25]

EPTable = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9,
           8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17,
           16, 17, 18, 19, 20, 21, 20, 21, 22, 23, 24, 25,
           24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]

Key56Table = [57, 49, 41, 33, 25, 17, 9,
              1, 58, 50, 42, 34, 26, 18,
              10, 2, 59, 51, 43, 35, 27,
              19, 11, 3, 60, 52, 44, 36,
              63, 55, 47, 39, 31, 23, 15,
              7, 62, 54, 46, 38, 30, 22,
              14, 6, 61, 53, 45, 37, 29,
              21, 13, 5, 28, 20, 12, 4]
Key48Table = [14, 17, 11, 24, 1, 5,
              3, 28, 15, 6, 21, 10,
              23, 19, 12, 4, 26, 8,
              16, 7, 27, 20, 13, 2,
              41, 52, 31, 37, 47, 55,
              30, 40, 51, 45, 33, 48,
              44, 49, 39, 56, 34, 53,
              46, 42, 50, 36, 29, 32]
Permute32 = [16, 7, 20, 21, 29, 12, 28, 17,
             1, 15, 23, 26, 5, 18, 31, 10,
             2, 8, 24, 14, 32, 27, 3, 9,
             19, 13, 30, 6, 22, 11, 4, 25]

# S Boxes
s1 = [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
      0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
      4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
      15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]

s2 = [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10,
      3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
      0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15,
      13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]

s3 = [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8,
      13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1,
      13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7,
      1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]

s4 = [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15,
      13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9,
      10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4,
      3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]

s5 = [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9,
      14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6,
      4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14,
      11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]

s6 = [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11,
      10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8,
      9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6,
      4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]

s7 = [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1,
      13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
      1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2,
      6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
s8 = [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7,
      1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2,
      7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8,
      2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]

# Shifts for Each Key
shifts = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
S = [s1, s2, s3, s4, s5, s6, s7, s8]

# Get binary string of x of length n
get_bin = lambda x, n: format(x, 'b').zfill(n)


def permute(key, perm):
    """
    Permute the given string according to the permutation list
    :param key: String to be permuted
    :param perm: Order of permutation
    :return: Permuted bit string
    """
    p = ""
    for i in perm:
        p += key[i - 1]
    return p

## Four Keys are stored in this table
KEYS = []


def round_shift(key_left, key_right):
    """
    Rotates two halves of a bit string with 1 place left
    :param key_left: Left half
    :param key_right: Right Half
    :return: Rotated left and right half
    """
    rotate_left = key_left[1:]
    rotate_left += key_left[:1]

    rotate_right = key_right[1:]
    rotate_right += key_right[:1]
    return rotate_left, rotate_right


# Tables to store the rotated halves
C = []
D = []


def generate_keys(key):
    """
    Given an integer key generate 16 sub keys.
    Stores the sub keys in the KEY table
    :param key: integer key
    :return: nothing.
    """
    key_string = get_bin(key, 64)
    #print(key_string)
    key_56 = permute(key_string, Key56Table)
    #print("Key 56: ", key_56)
    KEYS.append(key_56)
    C.append(key_56[:28])
    D.append(key_56[-28:])
    for i in range(1, 17):
        C0 = C[i - 1]
        D0 = D[i - 1]
        #print(i, shifts[i-1])
        if shifts[i - 1] == 1:
            Ci, Di = round_shift(C0, D0)
        elif shifts[i - 1] == 2:
            Ci, Di = round_shift(C0, D0)
            Ci, Di = round_shift(Ci, Di)

        #print("C: ", Ci)
        #print("D: ", Di)
        C.append(Ci)
        D.append(Di)
        Ki = permute(Ci + Di, Key48Table)
        KEYS.append(Ki)


def xor(a, b):
    """
    Xors two bit strings.
    :param a: First bit string
    :param b: Second bit string
    :return: XORed result
    """
    result = ""
    for i in range(len(a)):
        if a[i] == b[i]:
            result += "0"
        else:
            result += "1"
    return result


def SBox_lookup(bits, table):
    """
    Looks up given S Box. The bit string is of length 6.
    First and last bit give the row number
    2n,d 3rd, 4th and 5th bits give the column number
    :param bits: 6 bit string
    :param table: Sbox that needs to be looked up
    :return: 4 bit binary string
    """
    row = int(bits[0] + bits[5], 2)
    col = int(bits[1] + bits[2] + bits[3] + bits[4], 2)
    index = row * 16 + col
    return get_bin(table[index], 4)


def f(right, keyi):
    """
    f function which takes the right half and subkey.
    The right half is expanded to 48 bits and XORed with
    the sub key. The output is then sliced in to 6 bit strings
    where each string is an input for S box look up. All the outputs
    from the S box are combined to form 32 bit string. It is permuted
    before returned
    :param right: right half
    :param keyi: subkey
    :return: bit string
    """
    expanded_right = permute(right, EPTable)
    expRXORKey = xor(expanded_right, keyi)
    C = ""
    for i in range(0, 8):
        bits6 = expRXORKey[i * 6:(i + 1) * 6]
        c = SBox_lookup(bits6, S[i])
        C = C + c
    perm_C = permute(C, Permute32)
    return perm_C


def F(left, right, keyi):
    """
    The left half and output from the f function is
    XORed and swapped before returning
    :param left: left half
    :param right: right half
    :param keyi: subkey
    :return: right half, left key
    """
    left = xor(left, f(right, keyi))
    return right, left


def encrypt(pt):
    """
    Encrypts given input
    :param pt: Integer input to be encrypted string.
    :return: encrypted cipher
    """
    plaintext = get_bin(pt, 64)
    # initial permutation
    pt_init_perm = permute(plaintext, IP)
    # Left and right halves
    left = pt_init_perm[:32]
    right = pt_init_perm[-32:]
    # 16 rounds
    for i in range(1, 17):
        left, right = F(left, right, KEYS[i])
    # Final Permutation
    cipher = permute(right + left, IPinv)
    return hex(int(cipher, 2))[2:]


def decrypt(cipher):
    """
    Decrypt a give cipher
    :param cipher: cipher to be decrypted
    :return: decrypted message
    """
    cipher = get_bin(cipher, 64)
    pt_init_perm = permute(cipher, IP)
    left = pt_init_perm[:32]
    right = pt_init_perm[-32:]
    for i in range(16, 0, -1):
        left, right = F(left, right, KEYS[i])

    plaintext = permute(right + left, IPinv)
    return hex(int(plaintext, 2))[2:]


def main():
    key = '133457799BBCDFF1'
    message = '0123456789ABCDEF'
    print("Key: ", key)
    print("Message: ", message)
    generate_keys(int(key, 16))
    print("Generated Keys: ", KEYS)
    cipher = encrypt(int(message, 16))
    print("Cipher: ",cipher)
    decryptedM = decrypt(int(cipher, 16))
    print("Decrypted Message: ", decryptedM)
    print("Enter your Values now to test: ")
    KEYS.clear()
    key = input("Key in hex: ")
    message = input("Message in hex: ")
    print("Key: ", key)
    print("Message: ", message)
    generate_keys(int(key, 16))
    print("Generated Keys: ", KEYS)
    cipher = encrypt(int(message, 16))
    print("Cipher: ", cipher)
    decryptedM = decrypt(int(cipher, 16))
    print("Decrypted Message: ", decryptedM)

if __name__== "__main__":
  main()
