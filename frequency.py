import numpy as np


def get_text():
    filename = input("Enter filename: ")
    f = open(filename, "r")
    text = f.read()

    return text.upper()


def analyze(text):
    freq = np.zeros(26)

    for c in text:
        index = ord(c) - 65
        if 0 <= index < 26:
            freq[index] += 1

    sum = freq.sum()
    for i in range(26):
        freq[i] /= sum
    return freq


def print_analysis(freq):
    for i in range(26):
        print(chr(i+65), " : ", freq[i])

    sortedFreq = np.argsort(freq)
    print("Max #1 : ", chr(sortedFreq[-1] + 65), " ", freq[sortedFreq[-1]])
    print("Max #2 : ", chr(sortedFreq[-2] + 65), " ", freq[sortedFreq[-2]])
    return chr(sortedFreq[-1] + 65), chr(sortedFreq[-2] + 65)
    # return freq[sortedFreq[-1]], freq[sortedFreq[-2]], freq[sortedFreq[-3]]


#text = get_text()
#freq = analyze(text)
#print_analysis(freq)