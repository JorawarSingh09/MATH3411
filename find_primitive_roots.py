from math import gcd

def primRoots(modulo):
    roots = []
    required_set = set(num for num in range (1, modulo) if gcd(num, modulo) == 1)

    for g in range(1, modulo):
        actual_set = set(pow(g, powers) % modulo for powers in range (1, modulo))
        if required_set == actual_set:
            roots.append(g)           
    return roots

if __name__ == "__main__":
    m = int(input("enter m: "))
    primitive_roots = primRoots(m)
    print(primitive_roots)