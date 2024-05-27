"""help(input) # ver o que componhe a função"""

"""def contador(i, f, p):
    c = i
    while c <= f:
        print(f"{c}", end="") 
        c += p
    print("FIM")

help(contador)"""

'''def testa(b):
    global a # palavra reservada de variavel global.
    a = 8
    b += 4
    c = 2
    print(f"A dentro valor {a}")
    print(f"B dentro valor {b}")
    print(f"C dentro valor {c}")

a = 5
testa(a)
print(f"A fora vale {a}")'''

def somar(a=0, b=0, c=0):
    s = a + b + c
    return s

r1 = somar(2, 5, 7)
r2 = somar(3,5)
r3 = somar(5)

print(f'Os resultados foram {r1}, {r2}, {r3}')

print(f"Soma {r1+3}")

