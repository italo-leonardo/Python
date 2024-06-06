cont100 = 0
cont50 = 0
cont20 = 0
cont10 = 0
cont5 = 0
cont2 = 0
cont1 = 0
valor = int(input())
total = valor

while valor > 0:
    if valor >= 100:
        valor -= 100
        cont100 +=1
    elif valor < 100 and valor >= 50:
        valor -= 50
        cont50 += 1
    elif valor < 50 and valor >= 20:
        valor -= 20
        cont20 += 1
    elif valor < 20 and valor >= 10:
        valor -= 10
        cont10 += 1
    elif valor < 10 and valor >=5:
        valor -= 5
        cont5 += 1
    elif valor < 5 and valor >=2:
        valor -= 2
        cont2 += 1
    else:
        valor -= 1
        cont1 += 1

print(total)
print(f'{cont100} nota (s) de R$ 100,00')
print(f'{cont50} nota (s) de R$ 50,00')
print(f'{cont20} nota (s) de R$ 20,00')
print(f'{cont10} nota (s) de R$ 10,00')
print(f'{cont5} nota (s) de R$ 5,00')
print(f'{cont2} nota (s) de R$ 2,00')
print(f'{cont1} nota (s) de R$ 1,00')