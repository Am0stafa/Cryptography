from art import *
import rich as rich
from rich.progress import track
import time
import inquirer
# from block_ciphers.AES import AES
# from block_ciphers.DES import DES
# from asymmetric_ciphers.RSA import runRSA
# from asymmetric_ciphers.diffieHellman import runDH
# from elliptic_curves.elliptic_curve import EllipticCurve
# from elliptic_curves.ECDH import runECDH
# from secret_sharing.SSS import SSS


art_1=text2art("Crypto")
print(art_1)

rich.print("[bold red]You can[/bold red] [blue]encrypt, decrypt, hash, digitally-sign, exchange-keys, secret-sharing[/blue]")

def progressBar(howLong):
    howLong = int(howLong) * 10
    for i in track(range(howLong), description="Loading..."):
        time.sleep(0.1)

progressBar(2)

def fromByteToStr(byte):
    try:
        return byte.decode('utf-8')
    except:
        return byte.decode('utf-8', 'ignore')

def fromStrToByte(str):
    try:
        return str.encode('utf-8')
    except:
        return str.encode('utf-8', 'ignore')

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
    print(enc)

def Decrypt():
    dec = [
    inquirer.List('decryption',
                    message="Type of Decryption?",
                    choices=['Classical','Block Cipher','Asymmetric Cipher','Elliptic Curve'],
                ),
    ]
    dec = inquirer.prompt(dec)["decryption"]
    print(dec)

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
    print(signType)

def ExchangeKeys():
    exchangeType = [
    inquirer.List('exchange',
                    message="Type of Exchange?",
                    choices=['Diffie-Hellman','ECDH'],
                ),
    ]
    exchangeType = inquirer.prompt(exchangeType)["exchange"]
    print(exchangeType)

def SecretSharing():
    secretType = [
    inquirer.List('secret',
                    message="Type of Secret Sharing?",
                    choices=['Shamir'],
                ),
    ]
    secretType = inquirer.prompt(secretType)["secret"]
    print(secretType)


questions = [
  inquirer.List('type',
                message="What do you want to do?",
                choices=['Encrypt','Decrypt','Hash','Sign','Exchange Keys','Secret Sharing'],
            ),
]
answers = inquirer.prompt(questions)["type"]

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





