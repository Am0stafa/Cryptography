from art import *
import rich as rich
from rich.progress import track
import time
import inquirer
from classical_ciphers.classicalCiphers import ClassicalCiphers
# from block_ciphers.AES import AES
# from block_ciphers.DES import DES
from asymmetric_ciphers.RSA import runRSA
from asymmetric_ciphers.diffieHellman import runDH
# from elliptic_curves.elliptic_curve import EllipticCurve
# from elliptic_curves.ECDH import runECDH
from secret_sharing.SSS import runSSS

#! algorithms
def caesar(message, key):
    if key == "":
        key = 3
    try:
        key = int(key)
    except:
        listOfStr = [ord(i) for i in key]
        key = sum(listOfStr)

    c = ClassicalCiphers()
    return c.caesarEncrypt(message, key)

def decryptCaesar(message, key):
    if key == "":
        key = 3
    try:
        key = int(key)
    except:
        listOfStr = [ord(i) for i in key]
        key = sum(listOfStr)

    c = ClassicalCiphers()
    return c.caesarDecrypt(message, key)

def vigenere(message, key):
    c = ClassicalCiphers()
    return c.vigenereEncrypt(message, key)

def decryptVigenere(message, key):
    c = ClassicalCiphers()
    return c.vigenereDecrypt(message, key)

def hill(message, key):
    c = ClassicalCiphers()
    return c.hillEncrypt(message, key)

def decryptHill(message, key):
    c = ClassicalCiphers()
    return c.hillDecrypt(message, key)

def xor(message, key):
    c = ClassicalCiphers()
    return c.xorEncrypt(message, key)

def decryptXor(message, key):
    c = ClassicalCiphers()
    return c.xorDecrypt(message, key)

def monoalphabetic(message, key):
    c = ClassicalCiphers()
    return c.monoalphabeticEncrypt(message, key)

def decryptMonoalphabetic(message, key):
    c = ClassicalCiphers()
    return c.monoalphabeticDecrypt(message, key)

def autokey(message, key):
    c = ClassicalCiphers()
    return c.autokeyEncrypt(message, key)

def decryptAutokey(message, key):
    c = ClassicalCiphers()
    return c.autokeyDecrypt(message, key)

def railfence(message, key):
    c = ClassicalCiphers()
    return c.railfenceEncrypt(message, key)

def decryptRailfence(message, key):
    c = ClassicalCiphers()
    return c.railfenceDecrypt(message, key)

def rowTransposition(message, key):
    c = ClassicalCiphers()
    return c.rowTranspositionEncrypt(message, key)

def decryptRowTransposition(message, key):
    c = ClassicalCiphers()
    return c.rowTranspositionDecrypt(message, key)

def columnTransposition(message, key):
    c = ClassicalCiphers()
    return c.columnTranspositionEncrypt(message, key)

def decryptColumnTransposition(message, key):
    c = ClassicalCiphers()
    return c.columnTranspositionDecrypt(message, key)

def affine(message, key):
    c = ClassicalCiphers()
    return c.affineEncrypt(message, key)

def decryptAffine(message, key):
    c = ClassicalCiphers()
    return c.affineDecrypt(message, key)

def adfgx(message, key):
    c = ClassicalCiphers()
    return c.adfgxEncrypt(message, key)

def decryptAdfgx(message, key):
    c = ClassicalCiphers()
    return c.adfgxDecrypt(message, key)




#! end of algorithms



art_1=text2art("Crypto")
print(art_1)

rich.print("[bold red]You can[/bold red] [blue]encrypt, decrypt, hash, digitally-sign, exchange-keys, secret-sharing[/blue]")

def progressBar(howLong):
    howLong = int(howLong) * 10
    for i in track(range(howLong), description="Loading..."):
        time.sleep(0.1)

progressBar(2)

def exit():
    print("Exiting...")
    progressBar(2)
    exit()

def clearTerminal():
    print("\033c")

def Encrypt():
    enc = [
    inquirer.List('encryption',
                    message="Type of Encryption?",
                    choices=['Classical','Block Cipher','Asymmetric Cipher','Elliptic Curve'],
                ),
    ]
    enc = inquirer.prompt(enc)["encryption"]

    if enc == "Classical":
        clearTerminal()
        Classical()
    elif enc == "Block Cipher":
        clearTerminal()
        BlockCipher()
    elif enc == "Asymmetric Cipher":
        clearTerminal()
        AsymmetricCipher()
    elif enc == "Elliptic Curve":
        clearTerminal()
        EllipticCurve()
    else:
        print("Error")

def Classical(decrypt=False):
    classical = [
    inquirer.List('classical',
                    message="Type of Classical Cipher?",
                    choices=['Caesar','Vigenere','Hill','XOR','Monoalphabetic','Autokey','RailFence','Row transposition','Column transposition','Affine','ADFGX']
                ),
    ]
    classical = inquirer.prompt(classical)["classical"]
    message, key = messageAndKey()
    if classical == "Caesar":
        clearTerminal()
        if decrypt:
            rich.print("Plain Text: [bold blue]" + decryptCaesar(message, key) + "[/bold blue]")
        else:
            rich.print("Cipher Text: [bold red]" + caesar(message, key) + "[/bold red]")

    elif classical == "Vigenere":
        clearTerminal()
        if decrypt:
            rich.print("Plain Text: [bold blue]" + decryptVigenere(message, key) + "[/bold blue]")
        else:
            rich.print("Cipher Text: [bold red]" + vigenere(message, key) + "[/bold red]")

    elif classical == "Hill":
        clearTerminal()
        if decrypt:
            rich.print("Plain Text: [bold blue]" + decryptHill(message, key) + "[/bold blue]")
        else:
            rich.print("Cipher Text: [bold red]" + hill(message, key) + "[/bold red]")

    elif classical == "XOR":
        clearTerminal()
        if decrypt:
            rich.print("Plain Text: [bold blue]" + decryptXor(message, key) + "[/bold blue]")
        else:
            rich.print("Cipher Text: [bold red]" + xor(message, key) + "[/bold red]")

    elif classical == "Monoalphabetic":
        clearTerminal()
        if decrypt:
            rich.print("Plain Text: [bold blue]" + decryptMonoalphabetic(message, key) + "[/bold blue]")
        else:
            rich.print("Cipher Text: [bold red]" + monoalphabetic(message, key) + "[/bold red]")

    elif classical == "Autokey":
        clearTerminal()
        if decrypt:
            rich.print("Plain Text: [bold blue]" + decryptAutokey(message, key) + "[/bold blue]")
        else:
            rich.print("Cipher Text: [bold red]" + autokey(message, key) + "[/bold red]")

    elif classical == "RailFence":
        clearTerminal()
        if decrypt:
            rich.print("Plain Text: [bold blue]" + decryptRailfence(message, key) + "[/bold blue]")
        else:
            rich.print("Cipher Text: [bold red]" + railfence(message, key) + "[/bold red]")

    elif classical == "Row transposition":
        clearTerminal()
        if decrypt:
            rich.print("Plain Text: [bold blue]" + decryptRowTransposition(message, key) + "[/bold blue]")
        else:
            rich.print("Cipher Text: [bold red]" + rowTransposition(message, key) + "[/bold red]")
    
    elif classical == "Column transposition":
        clearTerminal()
        if decrypt:
            rich.print("Plain Text: [bold blue]" + decryptColumnTransposition(message, key) + "[/bold blue]")
        else:
            rich.print("Cipher Text: [bold red]" + columnTransposition(message, key) + "[/bold red]")

    elif classical == "Affine":
        clearTerminal()
        if decrypt:
            rich.print("Plain Text: [bold blue]" + decryptAffine(message, key) + "[/bold blue]")
        else:
            rich.print("Cipher Text: [bold red]" + affine(message, key) + "[/bold red]")

    elif classical == "ADFGX":
        clearTerminal()
        if decrypt:
            rich.print("Plain Text: [bold blue]" + decryptAdfgx(message, key) + "[/bold blue]")
        else:
            rich.print("Cipher Text: [bold red]" + adfgx(message, key) + "[/bold red]")
    else:
        print("Error")

def Decrypt():
    dec = [
    inquirer.List('decryption',
                    message="Type of Decryption?",
                    choices=['Classical','Block Cipher','Asymmetric Cipher','Elliptic Curve'],
                ),
    ]
    dec = inquirer.prompt(dec)["decryption"]
    if dec == "Classical":
        clearTerminal()
        Classical(decrypt=True)



def BlockCipher():
    blockCipher = [
    inquirer.List('blockCipher',
                    message="Type of Block Cipher Encryption?",
                    choices=['AES','DES'],
                ),
    ]
    blockCipher = inquirer.prompt(blockCipher)["blockCipher"]
    
    if blockCipher == "AES":
        clearTerminal()
        AESChoice()
    elif blockCipher == "DES":
        clearTerminal()
        DESChoice()

def AsymmetricCipher():
    asymmetricCipher = [
    inquirer.List('asymmetricCipher',
                    message="Type of Asymmetric Cipher Encryption?",
                    choices=['RSA'],
                ),
    ]
    asymmetricCipher = inquirer.prompt(asymmetricCipher)["asymmetricCipher"]
    if asymmetricCipher == "RSA":
        clearTerminal()
        runRSA()

def EllipticCurve():
    ellipticCurve = [
    inquirer.List('ellipticCurve',
                    message="Type of Elliptic Curve Encryption?",
                    choices=['ECDH'],
                ),
    ]
    ellipticCurve = inquirer.prompt(ellipticCurve)["ellipticCurve"]
    print(ellipticCurve)

def Hash():
    hashType = [
    inquirer.List('hash',
                    message="Type of Hash?",
                    choices=['MD5','SHA-1','SHA-256','SHA-512'],
                ),
    ]
    hashType = inquirer.prompt(hashType)["hash"]
    print(hashType)

def Sign():
    signType = [
    inquirer.List('sign',
                    message="Type of Sign?",
                    choices=['RSA','ECDSA'],
                ),
    ]
    signType = inquirer.prompt(signType)["sign"]
    if signType == "RSA":
        clearTerminal()
        runRSA()

def ExchangeKeys():
    exchangeType = [
    inquirer.List('exchange',
                    message="Type of Exchange?",
                    choices=['Diffie-Hellman','ECDH'],
                ),
    ]
    exchangeType = inquirer.prompt(exchangeType)["exchange"]
    if exchangeType == "Diffie-Hellman":
        clearTerminal()
        runDH()

def SecretSharing():
    secretType = [
    inquirer.List('secret',
                    message="Type of Secret Sharing?",
                    choices=['Shamir'],
                ),
    ]
    secretType = inquirer.prompt(secretType)["secret"]
    if secretType == "Shamir":
        clearTerminal()
        runSSS()

def AESChoice():
    aes = [
    inquirer.List('aes',
                    message="Type of AES?",
                    choices=['ECB','CBC','CTR','CFB','OFB'],
                ),
    ]
    aes = inquirer.prompt(aes)["aes"]
    print(aes)

def DESChoice():
    pass


def messageAndKey():
    message = [
    inquirer.Text('message',
                    message="Enter your message",
                ),
    ]
    message = inquirer.prompt(message)["message"]

    key = [
    inquirer.Text('key',
                    message="Enter your key",
                ),
    ]
    key = inquirer.prompt(key)["key"]

    return message, key










questions = [
  inquirer.List('type',
                message="What do you want to do?",
                choices=['Encrypt','Decrypt','Hash','Sign','Exchange Keys','Secret Sharing'],
            ),
]
answers = inquirer.prompt(questions)["type"]


if __name__ == "__main__":
    if answers == "Encrypt":
        clearTerminal()
        Encrypt()
    elif answers == "Decrypt":
        clearTerminal()
        Decrypt()
    elif answers == "Hash":
        clearTerminal()
        Hash()
    elif answers == "Sign":
        clearTerminal()
        Sign()
    elif answers == "Exchange Keys":
        clearTerminal()
        ExchangeKeys()
    elif answers == "Secret Sharing":
        clearTerminal()
        SecretSharing()
    else:
        print("Invalid Choice")
        exit()





