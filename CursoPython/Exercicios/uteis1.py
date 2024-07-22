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