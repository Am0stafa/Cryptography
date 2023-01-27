import random
import math
import base64

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

    sqr = int(math.sqrt(n)) + 1

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
    while True:
        e = random.randint(1, totient)
        if gcd(e, totient) == 1:
            return e
    

def calculate_d(e, totient):
    for d in range(1, totient):
        if (d * e) % totient == 1:
            return d

def print_keys(e, d, n):
    print(f"Public key (e,n): ({e}, {n})")
    print(f"Private key (d,n): ({d}, {n})")

# def encrypt(message, e, n):
#     return pow(message, e, n)

# def decrypt(cipher, d, n):
#     return pow(cipher, d, n)


def encrypt(message, e, n):
    # if the message if number encrypt it directly
    if isinstance(message, int):
        return pow(message, e, n)

    # convert each character to ascii code and encrypt it
    array = [pow(ord(c), e, n) for c in message]
    # join the array separate by slash
    encode = '/'.join(map(lambda x: str(x), array))
    # base64 encode the string
    cipher = base64.b64encode(encode.encode('ascii'))
    return cipher
    


def decrypt(cipher, d, n):
    # if the cipher is number decrypt it directly
    if isinstance(cipher, int):
        return pow(cipher, d, n)

    # base64 decode the string
    base64_bytes = base64.b64decode(cipher)
    base64_message = base64_bytes.decode('ascii')
    # split the string by slash
    array = base64_message.split('/')
    # decrypt each character
    decode = ''.join([chr(pow(int(char), d, n)) for char in array])
    return decode


def convertToMessage(message):
    length = math.ceil(message.bit_length() / 8)
    return message.to_bytes(length, byteorder='little').decode()
    
def convertToNumber(word):
    return int.from_bytes(word.encode(), byteorder='little')

# function that check if the input from the terminal is a number or not
def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def digital_signature(message, d, n):
    return encrypt(message, d, n)

def verify_signature(signature, e, n):
    return decrypt(signature, e, n)


def runRSA():
    choice = input("Do you want to generate keys? encrypt/decrypt? digital signature? or verify signature? (g/e/d/ds/vs): ")
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
        if is_number(message):
            message = int(message)
        e = int(input("Enter e: "))
        n = int(input("Enter n: "))
        cipher = encrypt(message, e, n)
        print("Cipher: ", cipher)

    elif choice.strip().lower() == 'd':
        cipher = (input("Enter Cipher: "))
        if is_number(cipher):
            cipher = int(cipher)
        d = int(input("Enter d: "))
        n = int(input("Enter n: "))
        message = decrypt(cipher, d, n)
        print("Message: ", message)

    elif choice.strip().lower() == 'ds':
        message = (input("Enter message: "))
        if is_number(message):
            message = int(message)
        d = int(input("Enter d: "))
        n = int(input("Enter n: "))
        signature = digital_signature(message, d, n)
        print("Signature: ", signature)

    elif choice.strip().lower() == 'vs':
        signature = (input("Enter signature: "))
        if is_number(signature):
            signature = int(signature)
        e = int(input("Enter e: "))
        n = int(input("Enter n: "))
        message = verify_signature(signature, e, n)
        print("Message: ", message)
    
    else:
        print("Invalid choice")