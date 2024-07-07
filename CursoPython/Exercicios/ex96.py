def area(l, m):
    mult = l * m
    print(f'A área de um terreno {l:.2f}x{m:.2f} é de {mult}m2.')
print(' Controle de Terrenos')
print('-'*20)
area(float(input('LARGURA (m): ')), float(input('COMPRIMENTO (m): ')))