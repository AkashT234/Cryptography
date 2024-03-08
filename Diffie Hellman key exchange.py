from random import randint
 
if __name__ == '__main__':
    P, G = 23, 9
    print(f'The Value of P is: {P}')
    print(f'The Value of G is: {G}')
     
    a, b = 4, 3
    print(f'The Private Key a for Alice is: {a}')
    print(f'The Private Key b for Bob is: {b}')
     
    x, y = pow(G, a, P), pow(G, b, P)
     
    ka, kb = pow(y, a, P), pow(x, b, P)
     
    print(f'Secret key for the Alice is: {ka}')
    print(f'Secret Key for the Bob is: {kb}')
