from math import *
from frequency import *
import matplotlib.pyplot as plt

alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
             'H', "j", 'K', 'L', 'M', 'N', 'O',
             'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


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
        val = (ord(str[i]) + ord(key[i % len(key)]) - 130) % 26
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
        val = (ord(cistr[i]) - ord(key[i % len(key)]) + 26) % 26
        orig += chr(val + 65)

    return orig


def key_length(cipher):
    """
    Given a cipher predict the length of key. Prints
    to the screen all the coincidences and a plot. User
    can look at them and input the key to the nextx function to find the key
    :param cipher: cipher to be analyzed
    :return: nothing
    """
    possible_lengths = range(1, 100)
    counts = []

    for length in possible_lengths:
        count = 0
        for i in range(length, len(cipher)):
            if cipher[i] == cipher[i - length]:
                count += 1
        counts.append(count)
    plt.plot(possible_lengths, counts)
    print(counts)
    plt.show()


def find_key(text, length, a):
    """
    Takes in cipher, expected length of the key and list of frequencies of English alphabets.
    :param text: cipher to be analyzed
    :param length: expected length of the key
    :param a: list of frequencies of English alphabets
    :return:
    """
    W = []  # all W matrices

    for j in range(length):
        temp = ""
        for i in range(len(text)):
            if i % length == 0 and i + j < len(text):
                temp += text[i + j] # append all i mod n charcters
        w = analyze(temp.upper()) # analyze their frequency
        W.append(w) # Append it to W matrix

    possibleKey = []
    for j in range(length):
        value = 0 #initalize
        k = 0
        for i in range(1, 26): # try all possible shifts
            rotate_i = np.array(a[i:]).tolist() + np.array(a[:i]).tolist()
            dot = np.dot(np.array(W[j][:]), np.array(rotate_i)) # dot product
            if dot > value: # find the max
                value = dot
                k = 26 - i
        if k < 8:
            possibleKey.append(alphabets[k]) # append the key chars
        else:
            possibleKey.append(alphabets[k-1])
    print("Hacked Key", possibleKey)


def get_text():
    filename = input("Enter filename from your folder: ")
    f = open(filename, "r")
    text = f.read()

    return text.upper()


def main():
    str = get_string()
    key = get_key()
    cipher = vigenere_encode(str, key)
    decipher = vigenere_decode(cipher, key)
    print(cipher)
    print(decipher)
    print("Input Large text file for Vigener Attack")
    str = get_text()
    key = get_key()
    cipher = vigenere_encode(str, key)
    a = analyze(str)
    key_length(cipher)
    length = input("What Key length did you observe in the plot or terminal output: ")
    length = int(length)
    find_key(cipher, length, a)



if __name__ == "__main__":
    main()
