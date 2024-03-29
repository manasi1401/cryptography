#################################################
# Author: Manasi Paste
# Course: Cryptography
# Professor: Dr. Karlsson
#
# Description: This program reads in a file and analyzes
# frequency of all English Alphabets. Its also prints the
# two highest frequencies.
# Requirements: Numpy
#
# Run instructions: python frequency.py
#################################################
import numpy as np


def get_text():
    filename = input("Enter filename from your folder: ")
    f = open(filename, "r")
    text = f.read()

    return text.upper()


def analyze(text):
    """
    Construct a 26 length array and increment count
    as you see a the character in the text
    :param text: text to be analyzed
    :return: array with frequencies of 26 letters.
    """
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
    """
    Print and return top two frequencies
    :param freq: array with frequencies of 26 letters.
    :return:top two frequency characters.
    """
    for i in range(26):
        print(chr(i+65), " : ", freq[i])

    sortedFreq = np.argsort(freq)
    print("Max #1 : ", chr(sortedFreq[-1] + 65), " ", freq[sortedFreq[-1]])
    print("Max #2 : ", chr(sortedFreq[-2] + 65), " ", freq[sortedFreq[-2]])
    return chr(sortedFreq[-1] + 65), chr(sortedFreq[-2] + 65)
    # return freq[sortedFreq[-1]], freq[sortedFreq[-2]], freq[sortedFreq[-3]]


def main():
    text = get_text()
    freq = analyze(text)
    print_analysis(freq)


if __name__== "__main__":
  main()