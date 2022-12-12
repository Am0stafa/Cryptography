import random
from math import sqrt
from Crypto.Util.number import *

def generate_prime_numbers():
    p = random_prime(100,1000)
    q = random_prime(100,1000)
    return p, q

def random_prime(a, b):
    while True:
        n = random.randint(a, b)
        if is_prime(n):
            return n

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def calculate_totient(p, q):
    return (p - 1) * (q - 1)

def calculate_n(p, q):
    return p * q

def calculate_e(totient):
    for e in range(2, totient):
        if gcd(e, totient) == 1:
            return e


def calculate_d(e, totient):
    for d in range(1, totient):
        if (d * e) % totient == 1:
            return d

def print_keys(e, d, n):
    print(f"Public key (e,n): ({e}, {n})")
    print(f"Private key (d,n): ({d}, {n})")

def encrypt(message, e, n):
    return pow(message, e) % n

def decrypt(cipher, d, n):
    return pow(cipher, d) % n

#TODO: error handling
def convertToMessage(message):
    return long_to_bytes(message).decode("utf-8") 
    #finally convert from bytes to string
    
def convertToNumber(word):
    return bytes_to_long(bytes(word, 'utf-8'))
    #finally convert from string to bytes


if __name__ == '__main__':
    choice = input("Do you want to generate keys? or encrypt/decrypt? (g/e/d): ")
    if choice.strip().lower() == 'g':
        p, q = generate_prime_numbers()
        print("Prime numbers: ", p, q)
        n = calculate_n(p, q)
        print("n: ", n)
        totient = calculate_totient(p, q)
        print("totient: ", totient)
        e = calculate_e(totient)
        d = calculate_d(e, totient)
        print_keys(e, d, n)
    elif choice.strip().lower() == 'e':
        message = (input("Enter message: "))
        if message.isnumeric():
            message = int(message)
        else:
            message = convertToNumber(message)
        e = int(input("Enter e: "))
        n = int(input("Enter n: "))
        cipher = encrypt(message, e, n)
        print("Cipher: ", cipher)
    elif choice.strip().lower() == 'd':
        cipher = int(input("Enter Cipher: "))
        d = int(input("Enter d: "))
        n = int(input("Enter n: "))
        message = decrypt(cipher, d, n)
        output = convertToMessage(message)
        print("Message: ", output)
    


