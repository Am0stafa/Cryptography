import math
import random
import time

def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a

# generate all the primitive roots of a function
def primRoots(modulo):
    roots = []
    required_set = set(num for num in range (1, modulo) if gcd(num, modulo) == 1)

    for g in range(1, modulo):
        actual_set = set(pow(g, powers) % modulo for powers in range (1, modulo))
        if required_set == actual_set:
            roots.append(g)           
    return roots

#generate prime numbers not greater than 500
def getAPrimeNumber():
    primes = []
    for possiblePrime in range(2, 600):
        isPrime = True
        for num in range(2, int(math.sqrt(possiblePrime)) + 1):
            if possiblePrime % num == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(possiblePrime)
    return random.choice(primes)


# generate the private key from the prime number
def generatePrivateKey(primeNumber):
    privateKey = random.randint(2, primeNumber)
    return privateKey

# calculate the public key
def calculatePublicKey(primeNumber, primitiveRoot, privateKey):
    publicKey = (primitiveRoot ** privateKey) % primeNumber
    return publicKey

#calculate the number that will be used to encrypt the message
def calculateEncryptionKey(primeNumber, bobsPublicKey, privateKey):
    encryptionKey = (bobsPublicKey ** privateKey) % primeNumber
    return encryptionKey

def runDH():
    choice = input("Do you want to generate every thing and just provide bobs public key? (y/N): ")
    if choice.lower() == "y":
        p = getAPrimeNumber()
        primitive_roots = primRoots(p)
        q = random.choice(primitive_roots)
        print(f"your prime number is {p} and your primitive root is {q}")
        time.sleep(2)
        privateKey = generatePrivateKey(p)
        print(f"your private key is {privateKey}")
        publicKey = calculatePublicKey(p, q, privateKey)
        print(f"your public key is {publicKey}")
        bobsPublicKey = int(input("Enter Bob's public key which can be between 2 and prime: "))
        key = calculateEncryptionKey(p, bobsPublicKey, privateKey)
        print(f"Key is {key}")
    else: 
        p = int(input("Enter your prime number: "))
        q = int(input("Enter your primitive root: "))
        privateKey = int(input("Enter your private key which between 2 and prime: "))
        print("Calculating public key...")
        publicKey = calculatePublicKey(p, q, privateKey)
        print(f"your public key is {publicKey}")
        bobsPublicKey = int(input("Enter Bob's public key: "))
        key = calculateEncryptionKey(p, bobsPublicKey, privateKey)
        print(f"Key is {key}")


