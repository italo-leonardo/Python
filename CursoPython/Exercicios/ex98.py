from time import sleep

def contagem(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-='*30)
    print(f'Contador de {i} até {f} de {p} em {p}')
    
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.3)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.3)
            cont -= p
        print('FIM!')
    print('-='*30)


contagem(1, 10, 1)
contagem(10,0,2)
print('Agora é sua vez de personalizar a contagem!')
inic = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contagem(inic, fim, pas)