from datetime import date
maior = 0
menor = 0
data_atual = date.today().year
for c in range(1, 8):
    data = int(input(f'Data de nacimento da {c}º pessoa: '))
    s = data_atual - data
    if s >= 18:
        maior +=1
    if s < 18:
        menor +=1 
print('Ao total tivemos {} pessoas maior de idade.'.format(maior))
print('Ao total tivemos {} menor de idade.'.format(menor))
