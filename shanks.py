from cryptomath import *


def is_square(n):
    rt = floor(sqrt(n))
    rt = int(rt)
    if rt*rt == int(n):
        return True
    else:
        return False



k = [1, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

def shanks_sq(n,k):
    if is_prime(n) or is_square(n):
        return n
    p0 = floor(sqrt(k*n))
    p_prev = p0
    q0 = 1
    q1 = k*n - p0*p0
    p1 = 0
    i = 2
    while is_square(q1) is False:
        temp = q1
        b = floor((p0+p_prev)/q1)
        p1 = b*q1-p_prev
        q1 = q0+b*(p_prev - p1)
        i += 1
        q0 = temp
        p_prev = p1
        if i > sqrt(n):
            break

    b = floor((p0-p1)/sqrt(q1))
    p0 = b*sqrt(q1) + p1
    p1 = p_prev = p0
    q0 = sqrt(q1)
    q1 = (k*n - p_prev*p_prev)/q0
    i = 0
    while True:
        b = floor((p0 + p1)/q1)
        p_prev = p1
        temp = q1
        p1 = b*q1 - p1
        q1 = q0 + b * (p_prev - p1)
        i += 1
        q0 = temp
        if p1 == p_prev:
            break
        if i > sqrt(n):
            break
    f = gcd(n, p1)
    f = int(f)
    if f is not 1 and f is not n:
        return f
    return 0

def factorize(n):
    for i in k:
        f = shanks_sq(n,i)
        print(i)
        if f is not 0:
            return f, n/f
    return 1, n



a = random_prime(5)
b = random_prime(3)
print(a,b)
print("f",factorize(a*b))
print("f",factorize(61*13))
print("f",factorize(111111111111))
print("f",factorize(881111111))
print("f",pollard_p_1(659699911))
print("f",factorize(100000))