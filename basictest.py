#################################################
# Author: Manasi Paste
# Course: Cryptography
# Professor: Dr. Karlsson
#
# Description: This program lets user test and
# interact with all the functions in the cryptomath library
#
# Run instructions: python basictest.py
#################################################
from cryptomath import *


def getTwoInt():
    a = input("Enter a: ")
    b = input("Enter b: ")
    a = int(a)
    b = int(b)
    return a, b


def getThreeInt():
    a = input("Enter a: ")
    d = input("Enter d: ")
    n = input("Enter n: ")
    a = int(a)
    d = int(d)
    n = int(n)
    return a, d, n


def menu():
    print("1) GCD")
    print("2) Extended GCD")
    print("3) Modular Inverse")
    print("4) Modular Power")
    print("5) Primality Testing")
    print("6) Pollard Rho")
    print("7) Pollard P-1")
    print("8) Fermat's Method")
    print("9) Shank's Square Form")
    print("10) Modular Square Root")
    print("q) Quit")


def main():
    menu()
    choice = input("Enter Your Choice: ")
    while choice != 'q' :
        if choice == '1':
            print("Testing GCD Function: ")
            a, b = getTwoInt()
            print("GCD of ", a, b, ": ", gcd(a,b))
        if choice == '2':
            print("Testing Extended GCD Function: ")
            a, b = getTwoInt()
            print("Extended GCD of ", a, b, ": g, x, y = ", extendedgcd(a, b))

        elif choice =='3':
            print("Testing Modular Inverse, a^-1 mod b : ")
            a, b = getTwoInt()
            print("a^-1 mod b ", a, b, ": ", findModInverse(a, b))
        elif choice is '4':
            print("Testing Modular Power, a^d mod n : ")
            a, d, n = getThreeInt()
            print("a^d mod n ", a, d, n, ": ", powerModulus(a, d, n))
        elif choice is '5':
            print("Primality Testing: ")
            print("Is ",2441, "a prime: ", is_prime(2441))
            print("Is ",2024861779763903, "a prime: ", is_prime(2024861779763903))
            print("Is ",455927, "a prime: ", is_prime(455927))

            a = input("Enter a number you want to test for prime: ")
            a = int(a)
            print("Is ", a, "a prime: ", is_prime(a))
        elif choice is '6':
            print("Pollard Rho Testing")
            a = input("Enter a number you want to factorize: ")
            a = int(a)
            print("Factor: ", pollard_rho(a))
        elif choice is '7':
            print("Pollard P-1 Testing")
            a = input("Enter a number you want to factorize: ")
            a = int(a)
            print("Factor: ", pollard_p_1(a))
        elif choice is '8':
            print("Fermat's method Testing")
            a = input("Enter a number you want to factorize: ")
            a = int(a)
            print("Factor: ", fermats_method(a))
        elif choice is '9':
            print("Shanks Square Form Testing")
            a = input("Enter a number you want to factorize: ")
            a = int(a)
            print("Factor: ", ShanksSquareForm(a))
        elif choice == '10':
            print("Testing Modular Square root, a^1/2 mod b : ")
            a, b = getTwoInt()
            print("a^1/2 mod b ", a, b, ": ", modular_sqr_root(a, b))

        print("_____________________________________________")
        print()
        choice = input("Enter Your Choice: ")
        menu()


if __name__== "__main__":
  main()