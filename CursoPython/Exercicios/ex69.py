idade = cont = cont_1 = cont_2 = 0
sexo = perguta = ''
while True:
    print("-"*30)
    print('CADASTRE UMA PESSOA')
    print('-'*30)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [F/M] ')).upper().strip()[0]
    if idade >= 18:
        cont += 1
    if sexo == "M":
        cont_1 += 1
    if sexo == "F" and idade < 18:
        cont_2 += 1
        
    perguta = ' '   
    while perguta not in 'SN':
        perguta = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if perguta == "N":
        break 
print(f'Total de pessoas com mais de 18 anos: {cont}')
print(f'Ao todo temos {cont_1} homens cadastrados')
print(f'E temos {cont_2} mulheres com menos de 20 anos')