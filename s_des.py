# Permutation Tables
# 1) IP
IP = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
# 2) Permute 8 bits by removing the 1st 2 bits from 10 bits
Perm10_8 =[6, 3, 7, 4, 8, 5, 10, 9]
# 3) Permute 8 bits
P8 = [2, 6, 3, 1, 4, 8, 5, 7]
# 4) IP inverse
IP_inv = [4, 1, 3, 5, 7, 2, 8, 6]
# 5) Expansion Table
EP = [4, 1, 2, 3, 2, 3, 4, 1]
# 6) Permute 4 bits
P4 =[2, 4, 3, 1]
# Sbox 1
s1 =[[1, 0, 3, 2], [3, 2, 1, 0], [0, 2, 1, 3],
     [0, 2, 1, 3], [3, 1, 3, 2]]
# SBox 2
s2 =[[0, 1, 2, 3], [2, 0, 1, 3], [3, 0, 1, 0],
     [2, 1, 0, 3]]

# 16 Keys are stored in this table
KEYS = []
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
        p +=key[i-1]
    return p


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


def xor(a, b):
    """
    Xors two bit strings.
    :param a: First bit string
    :param b: Second bit string
    :return: XORed result
    """
    result = ""
    for i in range(len(a)):
        if a[i] == b [i]:
            result += "0"
        else:
            result +="1"
    return result


def look_up_stable(bits, table):
    """
    Looks up given S Box. The bit string is of length 4.
    First and last bit give the row number
    2nd and 3rd bits gives the column number
    :param bits: 4 bit string
    :param table: Sbox that needs to be looked up
    :return: 2 bit binary string
    """
    r = int(bits[0]+bits[3], 2)
    c = int(bits[1]+bits[2], 2)
    return get_bin(table[r][c], 2)


def generateKeys(key):
    """
    Given an integer key generate 4 sub keys.
    Stores the sub keys in the KEY table
    :param key: integer key
    :return: nothing.
    """
    key_string = get_bin(key, 10)
    p = permute(key_string, IP)
    key_left = p[0:5]
    key_right = p[-5:]
    rKey_left, rKey_right = round_shift(key_left, key_right)
    keyOne = permute(rKey_left+rKey_right, Perm10_8)

    rKey_left, rKey_right = round_shift(rKey_left, rKey_right)
    keyTwo = permute(rKey_left+rKey_right, Perm10_8)

    rKey_left, rKey_right = round_shift(rKey_left, rKey_right)
    rKey_left, rKey_right = round_shift(rKey_left, rKey_right)
    keyThree = permute(rKey_left+rKey_right, Perm10_8)

    rKey_left, rKey_right = round_shift(rKey_left, rKey_right)
    rKey_left, rKey_right = round_shift(rKey_left, rKey_right)
    keyFour = permute(rKey_left+rKey_right, Perm10_8)

    KEYS = [keyOne, keyTwo, keyThree, keyFour]
    return KEYS


def encrypt_des(plain_text, KEYS):
    """
    Encrypt the given integer
    :param plain_text: integer to be encrypted
    :return: cipher
    """
    pt_bits = get_bin(plain_text, 8)
    perm_bits = permute(pt_bits, P8)
    left = perm_bits[:4]
    right = perm_bits[-4:]

    # Round 1
    st1L, st1R = feistal(left, right, KEYS[0])
    # Round 2
    st2L, st2R = feistal(st1L, st1R, KEYS[1])
    # Round 3
    st3L, st3R = feistal(st2L, st2R, KEYS[2])
    # Round 4
    st4L, st4R = feistal(st3L, st3R, KEYS[3])

    cipher = permute(st4R+st4L, IP_inv)
    return int(cipher, 2)


def decrypt_des(cipher, KEYS):
    """
    Decrypting given cipher
    :param cipher: cipher to be decrypted
    :return: decrypted cipher
    """
    pt_bits = get_bin(cipher, 8)
    perm_bits = permute(pt_bits, P8)
    left = perm_bits[:4]
    right = perm_bits[-4:]

    # Round 1
    # print("Round # 1")
    # print("input: ", left, right)
    st1L, st1R = feistal(left, right, KEYS[3])
    # Round 2
    # print("Round #2")
    # print("input: ", st1L, st1R)
    st2L, st2R = feistal(st1L, st1R, KEYS[2])
    # Round 3
    # print("Round #3")
    # print("input: ",st2L, st2R )
    st3L, st3R = feistal(st2L, st2R, KEYS[1])
    # Round 4
    # print("Round #4")
    # print("input: ", st3L, st3R)
    st4L, st4R = feistal(st3L, st3R, KEYS[0])

    plainText = permute(st4R + st4L, IP_inv)
    return int(plainText,2)


# Expansion Function and Permute
def expand_perm(r, k):
    """
    Xors right half and the key. First of the output feeds
    into SBox 1 and 2nd half feeds into the SBOX 2. The output
    combined and permuted before returning.
    :param r: right half
    :param k: subkey
    :return: bit string
    """
    expand_r = permute(r, EP)
    expand_r_xor_k = xor(expand_r, k)
    e_l = expand_r_xor_k[:4]
    e_r = expand_r_xor_k[-4:]

    sleft = look_up_stable(e_l, s1)
    sright = look_up_stable(e_r, s2)
    perm4 = permute(sleft + sright, P4)
    return perm4


def feistal(left, right, k):
    """
    The left half and output from the f function is
    XORed and swapped before returning
    :param left: left half
    :param right: right half
    :param k: subkey
    :return: right half, left key
    """
    l_xor_perm = xor(left, expand_perm(right, k))
    # print("Left XOR Exp_Perm(right, key): ", l_xor_perm)
    return right, l_xor_perm


def encryptText(t, key):
    """
    Encrypt a string using DES
    :param t: String to be encrypted
    :param key: Key to be used
    :return: cipher
    """
    t = t.lower()
    cipher = ""
    Keys = generateKeys(key)
    for p in t:
        i = encrypt_des(ord(p), Keys)
        cipher += chr(i)
    return cipher


def decryptText(c, key):
    """
    Decrypt a string using DES
    :param c: cipher to be decrypted
    :param key: Key to be used
    :return: decrypted message
    """
    pt=""
    Keys = generateKeys(key)
    for t in c:
        i = decrypt_des(ord(t), Keys)
        pt += chr(i)
    return pt


def main():
    key = 1000
    message = 123
    print("Key: ", key)
    print("Message: ", message)
    KEYS = generateKeys(key)
    print("Generated Keys: ", KEYS)
    print("Encrypting...")
    cipher = encrypt_des(message, KEYS)
    print("Cipher: ",cipher)
    print()
    print("Decrypting...")
    decryptedM = decrypt_des(cipher, KEYS)
    print("Decrypted Message: ", decryptedM)

if __name__== "__main__":
  main()
