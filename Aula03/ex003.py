n = int(input('Digite um numero de 3 digitos: '))

d = n / 100

print(d)
if d % 2 == 0:
    print('PAR')
else:
    print('IMPAr')