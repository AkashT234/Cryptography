def euclid(m, n):
    return m if n == 0 else euclid(n, m % n)

def exteuclid(a, b):
    r1, r2 = a, b
    s1, s2 = 1, 0
    t1, t2 = 0, 1
    while r2:
        q = r1 // r2
        r1, r2 = r2, r1 - q * r2
        s1, s2 = s2, s1 - q * s2
        t1, t2 = t2, t1 - q * t2
    return r1, t1 % a if t1 < 0 else t1

p, q = 823, 953
n, e = p * q, 313
Pn = (p - 1) * (q - 1)
key = [i for i in range(2, Pn) if euclid(Pn, i) == 1]
d = exteuclid(Pn, e)[1] if (r := exteuclid(Pn, e)[0]) == 1 else None
print(f"Decryption key is: {d}" if d else "Multiplicative inverse for the given encryption key does not exist. Choose a different encryption key")

M, S = 19070, pow(19070, d, n)
M1 = pow(S, e, n)
print("As M = M1, Accept the message sent by Alice" if M == M1 else "As M not equal to M1, Do not accept the message sent by Alice")
