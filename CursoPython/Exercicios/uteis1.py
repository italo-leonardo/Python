def metade(n, formato=False):
    m = n / 2
    return m if formato is False else moeda(m)

def dobro(n, formato=False):
    d = n * 2
    return d if formato is False else moeda(d)

def aumento(n, taxa, formato=False):
    v = n * (taxa/100)
    s  = v + n
    return s if formato is False else moeda(s)

def dimunuir(n, taxa, formato=False):
    di = n - (n * (taxa/100))
    return di if formato is False else moeda(di)

def moeda(n = 0, moeda = 'R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')

def retorno(n, formato=False):
    return n if formato is False else moeda(n)


def resumo(n):
    print('-'*30)
    print("RESUMO DO VALOR".center(30))
    print('-'*30)
    print(f'Preço analisado: \t{retorno(n, True)}')
    print(f'Dobro do preço: \t{dobro(n, True)}')
    print(f'Metade do preço: \t{metade(n, True)}')
    print(f'80% de aumento: \t{aumento(n, 80, True)}')
    print(f'35% de redução: \t{dimunuir(n, 35, True)}')
    print('-'*30)

def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg))
        if entrada.isalpha():
            print(f'ERRO:\"{entrada}\" é um preço invalido!')
        else:
            valido = True
            return float(entrada)