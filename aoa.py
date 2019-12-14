from rsa import *
from des import *
import time
import matplotlib.pyplot as plt
# RSA Keys
print("Generating keys for User 1 and User 2...")
rsa_key_gen_start_time = time.time()
user1_e, user1_n, user1_d = generate_keypair()
rsa_key_gen_end_time = time.time()
print("Time for RSA Key Gen: ", rsa_key_gen_end_time - rsa_key_gen_start_time)
user2_e, user2_n, user2_d = generate_keypair()
print()
print("User 1:")
print("Public Key (e, n): ", user1_e, user1_n)
print("Private key (d, n):" , user1_d, user1_n)
print("User 2:")
print("Public Key (e, n): ", user2_e, user2_n)
print("Private key (d, n):" , user2_d, user2_n)
print()
# Digital Signature
signature = 42
print("Agreed Signature: ", signature)
rsa_verification_start_time = time.time()
encrypt_signature = powerModulus(signature, user1_d, user1_n)
print("User 1 sends the encrypted signature using its private key: ", encrypt_signature)
print("User 2 decrypts the signature using User 1's public key...")
decrypted_signature = powerModulus(encrypt_signature, user1_e, user1_n)
print("Decrypted Signature: ", decrypted_signature)
if signature == decrypted_signature:
    print("Sender Verified")
rsa_verification_end_time = time.time()
print("Verification time: ", rsa_verification_end_time - rsa_verification_start_time)
print()
print()
# DES key
des_key = input("Choose DES Key: ")
des_key = int(des_key)
print("User 1 pick DES key: ", des_key)
print("Encrypting DES Key using RSA")

encrypted_des_key = powerModulus(des_key, user2_e, user2_n)
print("Encrypted DES using User2's public key: ", encrypted_des_key)

print("User2 decrypts DES Key sent by User 1...")
decrypted_des_key = powerModulus(encrypted_des_key, user2_d, user2_n)

print("Decrypted DES key: ", decrypted_des_key)

print()
print()

print("User 1 send encrypted message using DES...")
message = input("Enter your message: ")
# DES Encryption
print(message)
des_encrypt_start = time.time()
encrypted_des_message = encryptText(message, des_key)
des_encrypt_end = time.time()
print("Time for DES encryption: ", des_encrypt_end - des_encrypt_start)
print()
print("Encrypted message in DES: ", encrypted_des_message)
# DES decryption
print("User2 uses decrypted DES key to decrypt Sent Message")
des_decrypt_start = time.time()
decrypted_des_message = decryptText(encrypted_des_message, decrypted_des_key)
des_decrypt_end = time.time()
print("Time for DES decryption: ", des_decrypt_end - des_decrypt_start)
print("Decrypted Message by User 2: ",decrypted_des_message )

print("!!Verified user, decrypted message, safe key!! ")

# l = range(1, 1000)
# a = "a"
# #s = "HereIamagaintestingthiscodeforeverandeverandever"
# t = []
# for i in range(1, 1000):
#     s = a*i
#     user1_e, user1_n, user1_d = generate_keypair()
#     des_encrypt_start = time.time()
#     encrypt_rsa([user2_e, user1_n], s)
#     #encryptText(s, i)
#     des_encrypt_end = time.time()
#     t.append(des_encrypt_end - des_encrypt_start)
#
# plt.plot(l, t)
# plt.xlabel("Length of string (N)")
# plt.ylabel("Time in seconds (t)")
# plt.title("RSA: Length of String vs Time")
# plt.show()