
initPerm = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
perm8 =[6, 3, 7, 4, 8, 5, 10, 9]
pt_perm = [2, 6, 3, 1, 4, 8, 5, 7]
in_perm = [4, 1, 3, 5, 7, 2, 8, 6]
epTable = [4, 1, 2, 3, 2, 3, 4, 1]
p4Table =[2, 4, 3, 1]

s1 =[[1, 0, 3, 2], [3, 2, 1, 0], [0, 2, 1, 3],
     [0, 2, 1, 3], [3, 1, 3, 2]]

s2 =[[0, 1, 2, 3], [2, 0, 1, 3], [3, 0, 1, 0],
     [2, 1, 0, 3]]

get_bin = lambda  x, n: format(x, 'b').zfill(n)


def permute(key, perm):
    p = ""
    for i in perm:
        p +=key[i-1]
    return p


def get_key(key):
    # step1: convert to binary string
    key_string = get_bin(key, 10)
    # step2: permute the bits
    p = permute(key_string, initPerm)
    # step 3: return left and right half
    return p[0:5], p[-5:]


def round_shift(key_left, key_right):
    # step 4: roate each hald
    rotate_left = key_left[1:]
    rotate_left += key_left[:1]

    rotate_right = key_right[1:]
    rotate_right += key_right[:1]
    return rotate_left, rotate_right


def get_key_one(left, right):
    # step 5: combine the the two halves
    # permute them in P8 table
    combineBits = left+right
    result = permute(combineBits, perm8)
    return result


def xor(a, b):
    result = ""
    for i in range(len(a)):
        if a[i] == b [i]:
            result += "0"
        else:
            result +="1"
    return result

def get_key_two(left, right):
    first_left, first_right = round_shift(left, right)
    second_left, second_right = round_shift(first_left, first_right)
    combine_bits = second_left+second_right
    result = permute(combine_bits, perm8)
    return result


def look_up_stable(bits, table):
    r = int(bits[0]+bits[3], 2)
    c = int(bits[1]+bits[2], 2)
    return get_bin(table[r][c], 2)


def generateKeys(key):
    key_left, key_right = get_key(key)
    rKey_left, rKey_right = round_shift(key_left, key_right)
    keyOne = get_key_one(rKey_left, rKey_right)
    keyTwo = get_key_two(rKey_left, rKey_right)
    return keyOne, keyTwo


def encrypt_des(plain_text, key):
    pt_bits = get_bin(plain_text, 8)
    perm_bits = permute(pt_bits, pt_perm)
    left = perm_bits[:4]
    right = perm_bits[-4:]
    keyOne, keyTwo = generateKeys(key)

    # Round 1
    st1L, st1R = feistal(left, right, keyOne)
    # Round 2
    st2L, st2R = feistal(st1L, st1R, keyTwo)
    # Round 3
    st3L, st3R = feistal(st2L, st2R, keyOne)
    # Round 4
    st4L, st4R = feistal(st3L, st3R, keyTwo)

    cipher = permute(st4R+st4L, in_perm)
    return int(cipher, 2)


def decyrpt_des(cipher, key):
    pt_bits = get_bin(cipher, 8)
    perm_bits = permute(pt_bits, pt_perm)
    left = perm_bits[:4]
    right = perm_bits[-4:]
    keyOne, keyTwo = generateKeys(key)

    # Round 1
    st1L, st1R = feistal(left, right, keyTwo)
    # Round 2
    st2L, st2R = feistal(st1L, st1R, keyOne)
    # Round 3
    st3L, st3R = feistal(st2L, st2R, keyTwo)
    # Round 4
    st4L, st4R = feistal(st3L, st3R, keyOne)

    plainText = permute(st4R + st4L, in_perm)
    return int(plainText,2)


def expand_perm(r, k):
    expand_r = permute(r, epTable)
    expand_r_xor_k = xor(expand_r, k)
    e_l = expand_r_xor_k[:4]
    e_r = expand_r_xor_k[-4:]

    sleft = look_up_stable(e_l, s1)
    sright = look_up_stable(e_r, s2)
    combine = sleft + sright
    perm4 = permute(combine, p4Table)
    return perm4


def feistal(left, right, k):
    l_xor_perm = xor(left, expand_perm(right, k))
    return right, l_xor_perm


def encryptText(t, key):
    t = t.lower()
    cipher = ""
    for p in t:
        i = encrypt_des(ord(p), key)
        cipher += chr(i)
    return cipher

def decryptText(c, key):
    pt=""

    for t in c:
        i = decyrpt_des(ord(t), key)
        pt += chr(i)
    return pt


def get_round_14(bits, key):
    left = bits[:4]
    right = bits[-4:]
    keyOne, keyTwo = generateKeys(key)

    # Round 1
    #st1L, st1R = feistal(left, right, keyOne)
    # Round 2
    st2L, st2R = feistal(left, right, keyTwo)
    # Round 3
    st3L, st3R = feistal(st2L, st2R, keyOne)
    # Round 4
    st4L, st4R = feistal(st3L, st3R, keyTwo)

    return left, right, st4L, st4R


def differential_cryptanalysis3(first, first_star, key, count):
    print(generateKeys(key))

    l1,r1,l4,r4 = get_round_14(first, key)
    l1_star, r1_star, l4_star, r4_star = get_round_14(first_star, key)
    l1_diff = xor(l1, l1_star)
    r1_diff = xor(r1, r1_star)
    l4_diff = xor(l4, l4_star)
    r4_diff = xor(r4, r4_star) # = l1' xor f(r3, k2) xor (r3*,k2)
    # r3 = l4 and r3*= l4*

    # E(l4 xor l4*) = E(l4')
    expand_l4_diff = permute(l4_diff, epTable)
    s1_input = expand_l4_diff[:4]
    s2_input = expand_l4_diff[-4:]
    # r4' xor l1'
    r4_d_xor_l1_d = xor(r4_diff, l1_diff)
    s1_output = r4_d_xor_l1_d[:2]
    s2_output = r4_d_xor_l1_d[-2:]

    el4 = permute(l4, epTable)
    el4_left = el4[:4]
    el4_right = el4[-4:]
    el4_star = permute(l4_star, epTable)
    # find pairs s1
    for i in range(0, 16):
        for j in range(0, 16):
            x = get_bin(i, 4)
            y = get_bin(j, 4)
            if xor(x, y) == s1_input:
                s1_x = look_up_stable(x, s1)
                s1_y = look_up_stable(y, s1)
                if xor(s1_x, s1_y) == s1_output:
                    pairs_s1.append(xor(x, el4_left))


    # find pairs s2
    for i in range(0, 16):
        for j in range(0, 16):
            x = get_bin(i, 4)
            y = get_bin(j, 4)
            if xor(x, y) == s2_input:
                s2_x = look_up_stable(x, s2)
                s2_y = look_up_stable(y, s2)
                if xor(s2_x, s2_y) == s2_output:
                    pairs_s2.append(xor(y, el4_right))




e = encrypt_des(255, 642)
d = decyrpt_des(e, 642)
print ("encrypted", e)
print("decrypted", d)

e = encryptText("sdf", 222)
d = decryptText(e, 222)
print(e)
print(d)
first ="10001010"
first_star ="10101010"
key = 100
pairs_s1 =[]
pairs_s2 =[]
key_left = []
key_right = []
differential_cryptanalysis3(first, first_star, key, 0)
first ="11001011"
first_star ="10101011"
differential_cryptanalysis3(first, first_star, key, 1)
first ="10111011"
first_star ="10101011"
differential_cryptanalysis3(first, first_star, key, 2)
first ="11001011"
first_star ="11101011"
differential_cryptanalysis3(first, first_star, key, 2)
first ="10001011"
first_star ="10111011"
differential_cryptanalysis3(first, first_star, key, 2)
first ="00001011"
first_star ="11111011"
differential_cryptanalysis3(first, first_star, key, 2)
print(pairs_s1)
print(pairs_s2)

counterLeft = {}
counterRight = {}
for a in pairs_s1:
    if a in counterLeft:
        counterLeft[a] += 1
    else:
        counterLeft[a] = 1


for a in pairs_s2:
    if a in counterRight:
        counterRight[a] += 1
    else:
        counterRight[a] = 1
print(get_bin(key,8))
print(counterLeft)
print(counterRight)



