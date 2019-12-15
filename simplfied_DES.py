
initPerm = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
perm8 =[6, 3, 7, 4, 8, 5, 10, 9]
pt_perm = [2, 6, 3, 1, 4, 8, 5, 7]
perm_inv = [4, 1, 3, 5, 7, 2, 8, 6]
epTable = [4, 1, 2, 3, 2, 3, 4, 1]
p4Table =[2, 4, 3, 1]

s1 =[[1, 0, 3, 2], [3, 2, 1, 0], [0, 2, 1, 3],
     [0, 2, 1, 3], [3, 1, 3, 2]]

s2 =[[0, 1, 2, 3], [2, 0, 1, 3], [3, 0, 1, 0],
     [2, 1, 0, 3]]
KEYS = []

get_bin = lambda x, n: format(x, 'b').zfill(n)


def permute(key, perm):
    p = ""
    for i in perm:
        p +=key[i-1]
    return p


def round_shift(key_left, key_right):
    rotate_left = key_left[1:]
    rotate_left += key_left[:1]

    rotate_right = key_right[1:]
    rotate_right += key_right[:1]
    return rotate_left, rotate_right


def xor(a, b):
    result = ""
    for i in range(len(a)):
        if a[i] == b [i]:
            result += "0"
        else:
            result +="1"
    return result


def look_up_stable(bits, table):
    r = int(bits[0]+bits[3], 2)
    c = int(bits[1]+bits[2], 2)
    return get_bin(table[r][c], 2)


def generateKeys(key):
    key_string = get_bin(key, 10)
    p = permute(key_string, initPerm)
    key_left = p[0:5]
    key_right = p[-5:]
    rKey_left, rKey_right = round_shift(key_left, key_right)
    keyOne = permute(rKey_left+rKey_right, perm8)

    rKey_left, rKey_right = round_shift(rKey_left, rKey_right)
    keyTwo = permute(rKey_left+rKey_right, perm8)

    rKey_left, rKey_right = round_shift(rKey_left, rKey_right)
    rKey_left, rKey_right = round_shift(rKey_left, rKey_right)
    keyThree = permute(rKey_left+rKey_right, perm8)

    rKey_left, rKey_right = round_shift(rKey_left, rKey_right)
    rKey_left, rKey_right = round_shift(rKey_left, rKey_right)
    keyFour = permute(rKey_left+rKey_right, perm8)

    KEYS = [keyOne, keyTwo, keyThree, keyFour]
    return KEYS


def encrypt_des(plain_text):
    pt_bits = get_bin(plain_text, 8)
    perm_bits = permute(pt_bits, pt_perm)
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

    cipher = permute(st4R+st4L, perm_inv)
    return int(cipher, 2)


def decrypt_des(cipher):
    pt_bits = get_bin(cipher, 8)
    perm_bits = permute(pt_bits, pt_perm)
    left = perm_bits[:4]
    right = perm_bits[-4:]

    # Round 1
    st1L, st1R = feistal(left, right, KEYS[3])
    # Round 2
    st2L, st2R = feistal(st1L, st1R, KEYS[2])
    # Round 3
    st3L, st3R = feistal(st2L, st2R, KEYS[1])
    # Round 4
    st4L, st4R = feistal(st3L, st3R, KEYS[0])

    plainText = permute(st4R + st4L, perm_inv)
    return int(plainText,2)


def expand_perm(r, k):
    expand_r = permute(r, epTable)
    expand_r_xor_k = xor(expand_r, k)
    e_l = expand_r_xor_k[:4]
    e_r = expand_r_xor_k[-4:]

    sleft = look_up_stable(e_l, s1)
    sright = look_up_stable(e_r, s2)
    perm4 = permute(sleft + sright, p4Table)
    return perm4


def feistal(left, right, k):
    l_xor_perm = xor(left, expand_perm(right, k))
    return right, l_xor_perm

key = 100
message = 123
print("Message: ", message)
KEYS = generateKeys(key)
cipher = encrypt_des(message)
print("Cipher: ",cipher)
decryptedM = decrypt_des(cipher)
print("Decrypted Message: ", decryptedM)