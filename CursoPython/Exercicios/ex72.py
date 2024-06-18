num = ('zero','um', 'dois', 'tres', 'quatro')

while True:
    op = int(input('Digite um numero entre 0 e 4: '))
    if op < 0 or op > 4:
       print('Tente novamente.', end='')
    else:
        print(f'Vocé digitou o número {num[op]}')
        break

