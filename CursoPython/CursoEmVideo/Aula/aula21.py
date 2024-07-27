"""help(input) # ver o que componhe a função"""

'''def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: inicia da contaguem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno 
    Função criada por Italo Leonardo O Hack
    """
    c = i
    while c <= f:
        print(f"{c}", end="") 
        c += p
    print("FIM")

help(contador)'''

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


'''def somar(a=0, b=0, c=0):# especificar valor.
    s = a + b + c
    return s

r1 = somar(2, 5, 7)
r2 = somar(int(input('numero: ')),int(input('numero: ')))
r3 = somar(5)

print(f'Os resultados foram {r1}, {r2}, {r3}')

print(f"Soma {r1+3}")'''

'''def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')'''

def par(n=0):
    if n % 2 ==0:
        return True
    else:
        return False
    
num = int(input("digite um numero: "))
print(f'O numero {num} é par? {par(num)}')

