t = int(input('Quantos termos que ver: '))
p = int(input('Pular de quantos: '))
for x in range(t-1):
    if x == 0:
        print(f'1 Termo: {t}')
    ant = t
    t += p
    print(f'{x+2} Termo: {ant} + {p} = {t} ')
    
    