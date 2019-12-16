#################################################
# Author: Manasi Paste
# Course: AOA
# Professor: Dr. Rebenitsch
#
# Description: This program demonstrates an hybrid
# application of RSA and DES for secure communication.
# Second half of the project runs some built in tests
# to check the encryption functions for RSA, DES, Key generation
# for DES and understanding distribution of RSA keys
# Requirements: Numpy, Math and Matplotlib library
#
# Inputs: DES Key value and Message to be encoded
#
# Run instructions: python aoa.py
#################################################
from rsa import *
from s_des import *
import matplotlib.pyplot as plt


def secure_communication():
    # RSA Keys
    print("------------Key Generation----------------")
    user1_e, user1_n, user1_d = generate_keypair()
    user2_e, user2_n, user2_d = generate_keypair()
    print()
    print("Sender:")
    print("Public Key (e, n): ", user1_e, user1_n)
    print("Private key (d, n):" , user1_d, user1_n)
    print("Receiver:")
    print("Public Key (e, n): ", user2_e, user2_n)
    print("Private key (d, n):" , user2_d, user2_n)
    print()
    # Digital Signature
    print("------------Verification----------------")
    signature = 42
    print("Agreed Signature: ", signature)
    encrypt_signature = powerModulus(signature, user1_d, user1_n)
    print("Sender ----S1(signature) = Es----> Receiver: ", encrypt_signature)
    print("Receiver ----P1(Es) => Decrypted Signature: ")
    decrypted_signature = powerModulus(encrypt_signature, user1_e, user1_n)
    print("Decrypted Signature: ", decrypted_signature)
    if signature == decrypted_signature:
        print("Sender Verified")

    print()
    print()
    # DES key
    print("------------Key Communication Using RSA----------------")
    des_key = input("Choose DES Key(1-1023): ")
    des_key = int(des_key)
    print("Sender picked DES key: ", des_key)
    print("Encrypting DES Key using RSA")

    encrypted_des_key = powerModulus(des_key, user2_e, user2_n)
    print("Sender --- P2(DES_Key) = Ek ---> Receiver: ", encrypted_des_key)

    print("Receiver --- S2(Ek) => DES_Key")
    decrypted_des_key = powerModulus(encrypted_des_key, user2_d, user2_n)

    print("Decrypted DES key: ", decrypted_des_key)

    print()
    print()
    print("-------------DES Encryption----------------")
    message = input("Enter your message: ")
    # DES Encryption
    print("Sender --- DES(M, DES_Key) = E ---> Receiver")

    encrypted_des_message = encryptText(message, des_key)
    print("Encrypted message in DES: ", encrypted_des_message)
    # DES decryption
    print()
    print("-------------DES Decryption----------------")
    print("Receiver --- DES_Decrypt(E, DES_Key) = > M")
    decrypted_des_message = decryptText(encrypted_des_message, decrypted_des_key)
    print("Decrypted Message by Receiver: ",decrypted_des_message )

    print("!!Verified user, decrypted message, safe key!! ")

############################################################
# LOOK HERE TO TEST


# DES Encryption and decryption testing
def test_des(M, key):
    e = encryptText(M, key)
    d = decryptText(e, key)
    if d == M.lower():
        return True
    else:
        return False


# RSA key generation and decryption testing
def test_rsa(M):
    e, n, d = generate_keypair()
    cipher = encrypt_rsa([e,n], M)
    plaintext = decrypt_rsa([d,n], cipher)
    if M.upper() == plaintext:
        return True
    else:
        return False


# Looking at RSA key distribution
def rsa_distribuition(option):
    e =[]
    n = []
    d = []
    t = range(1,1000)
    for i in range(1, 1000):
        x, y, z = generate_keypair()
        e.append(x)
        n.append(y)
        d.append(z)
    if option == 1:
        plt.hist(n, facecolor="blue")
        plt.xlabel("N")
    if option == 2:
        plt.hist(e, facecolor="blue")
        plt.xlabel("e")
    if option == 3:
        plt.hist(d, facecolor="blue")
        plt.xlabel("d")
    plt.ylabel("Number of Times")
    plt.show()


# Stress testing DES (increase the range if you want to test more)
def stress_test_DES():
    a = "s"
    for i in range(1, 100):
        key = i
        s =a*i
        if test_des(s, key) is False:
            print("\tDES Failed for key, message: ", key, s )
            return
    print("\tStress testing DES successful")
    return

# Stress testing DES (increase the range if you want to test more)
def stress_test_RSA():
    a = "s"
    for i in range(1, 100):
        s =a*i
        if test_rsa(s) is False:
            print("\tRSA Failed for key, message: ", key, s )
            return
    print("\tStress testing RSA successful")
    return


# Perform all the tests
def tests():
    # LOOK HERE TO TEST
    des_key = 100
    message = "Ain't no sunshine!!"
    print("Test 1: Encryption - Decryption DES")
    if test_des(message, des_key):
        print("\tTest 1 passed")
    else:
        print("\tTest 1 failed")

    print("Test 2: Encryption - Decryption RSA")
    if test_rsa(message):
        print("\tTest 2 passed")
    else:
        print("\tTest 2 failed")
    print("Test 3: Stress Test DES")
    stress_test_DES()
    print("Test 4: Stress Test RSA")
    stress_test_RSA()

    print("Test 5: Analyze Distribution of RSA Generated Key (Press Q to close the graphs)")
    print("\tDistribution of N")
    rsa_distribuition(1)
    print("\tDistribution of e")
    rsa_distribuition(2)
    print("\tDistribution of d")
    rsa_distribuition(3)


def main():
    secure_communication()
    print()
    print("-------------Built In Test----------------")
    tests()

if __name__== "__main__":
  main()