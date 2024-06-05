idade = cont = cont_1 = cont_2 = 0
sexo = perguta = ''
while True:
    print("-"*30)
    print('CADASTRE UMA PESSOA')
    print('-'*30)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [F/M] ')).upper()
    if idade >= 18:
        cont += 1
    if sexo == "M":
        cont_1 += 1
    if sexo == "F" and idade < 18:
        cont_2 += 1
    perguta = str(input('Quer continuar? [S/N]')).upper()
    if perguta == "N":
        break 
print(f'Total de pessoas com mais de 18 anos: {cont}')
print(f'Ao todo temos {cont_1} homens cadastrados')
print(f'E temos {cont_2} mulheres com menos de 20 anos')