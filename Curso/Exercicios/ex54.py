maior = 0
menor = 0
for c in range(0, 7):
    data = int(input('Data de nacimento: '))
    s = 2024 - data
    if s >= 18:
        maior +=1
    else:
        menor +=1 
print('{} maior de idade.'.format(maior))
print('{} menor de idade.'.format(menor))
