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

if __name__ == "__main__":
    p = 23
    primitive_roots = primRoots(p)
    print(primitive_roots)