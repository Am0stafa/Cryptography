from sympy import GF, Poly
import random
from numpy.polynomial import Polynomial
# from scipy.interpolate import lagrange


class SSS:
    def __init__(self, n, t, prime):
        self.n = n # number of shares
        self.t = t # threshold where t <= n 
        self.prime = prime # prime number
        self.field = GF(prime) # finite field

    # def generate_shares(self):
    #     # generate random coefficients
    #     coefficients = [random.randint(1,self.prime-1) for i in range(self.t-1)]
    #     coefficients.append(self.secret)
    #     print(coefficients)

    #     # generate polynomial
    #     polynomial = Poly(coefficients, self.field)
    #     # generate shares
    #     shares = []
    #     for i in range(1,self.n+1):
    #         shares.append((i,polynomial(i)))
    #     return shares

    def generate_shares(self, secret):
        # generate random coefficients
        coefficients = [random.randint(1,self.prime-1) for i in range(self.t-1)]
        coefficients.append(secret)

        # generate polynomial
        polynomial = Polynomial(coefficients)
        # generate shares
        shares = []
        for i in range(1,self.n+1):
            shares.append((i,polynomial(i)))
        return shares

    def recover_secret(self, shares):
        # recover secret
        # polynomial = lagrange([i[0] for i in shares], [i[1] for i in shares])
        # return polynomial(0)
        polynomial = Polynomial.fit([i[0] for i in shares], [i[1] for i in shares], self.t-1)
        return polynomial(0)

if __name__ == "__main__":
    sss = SSS(5,3,7)
    shares = sss.generate_shares(14)
    print(shares)
    secret = sss.recover_secret(shares)
    print(secret)

