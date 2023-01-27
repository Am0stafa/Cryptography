from elliptic_curve import EllipticCurve
import random

class EllipticCurveDH:
    def __init__(self, a, b, p):
        self.curve = EllipticCurve(a, b, p)
        self.private_key = None
        self.public_key = None
        self.shared_key = None

    
    def generate_private_key(self):
        self.private_key = random.randint(1, self.curve.number_of_points)
        return self.private_key
    
    def generate_public_key(self):
        self.public_key = self.curve.points[self.private_key]
        return self.curve.point_doubling(self.public_key, self.private_key)

    def generate_shared_key(self, b_public_key):
        self.shared_key = self.curve.point_doubling(b_public_key, self.private_key)
        return self.shared_key
    

if __name__ == "__main__": # to be changed to runECDH()
    a = 1
    b = 6
    p = 23
    alice = EllipticCurveDH(a, b, p)
    bob = EllipticCurveDH(a, b, p)
    alice.generate_private_key()
    bob.generate_private_key()
    alice.generate_public_key()
    bob.generate_public_key()
    alice.generate_shared_key(bob.public_key)
    bob.generate_shared_key(alice.public_key)
    print(alice.shared_key, bob.shared_key)

    